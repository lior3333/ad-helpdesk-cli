import os
import sys
import ssl
import socket
import subprocess
import platform
import concurrent.futures
from dotenv import load_dotenv
from ldap3 import Server, Connection, ALL, NTLM, Tls
from bidi.algorithm import get_display

from rich.console import Console,Group
from rich.table import Table
from rich.panel import Panel

console = Console()

load_dotenv()

AD_SERVER = os.getenv('AD_SERVER')
USER_DN = os.getenv('AD_USER')
PASSWORD = os.getenv('AD_PASSWORD')
SEARCH_BASE = os.getenv('AD_SEARCH_BASE')

def ping_host(hostname):
    current_os = platform.system().lower()
    
    if current_os == "windows":
        command = ['ping', '-n', '1', '-w', '1000', hostname]
    else:
        command = ['ping', '-c', '1', '-W', '1000', hostname]
        
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except Exception:
        return False

# 3. הפונקציה המרכזית: חיפוש עובד, שיוך מחשבים ובדיקת סטטוס
def search_user_and_computer(search_name):
    # הגדרת הצפנה (TLS) ופורט 636
    tls_configuration = Tls(validate=ssl.CERT_NONE, version=ssl.PROTOCOL_TLSv1_2)
    server = Server(AD_SERVER, port=636, use_ssl=True, tls=tls_configuration, get_info=ALL)
    
    # התחברות מאובטחת באמצעות NTLM
    try:
        conn = Connection(server, user=USER_DN, password=PASSWORD, authentication=NTLM, auto_bind=True)
    except Exception as e:
        print(f"[!] שגיאת התחברות לשרת: {e}")
        return

    #  שלב א: חיפוש העובד
    user_filter = f'(|(givenName={search_name}*)(displayName=*{search_name}*))'
    user_attributes = ['displayName', 'sAMAccountName', 'department', 'telephoneNumber', 'mail']
    
    conn.search(search_base=SEARCH_BASE, search_filter=user_filter, attributes=user_attributes)
    
    if not conn.entries:
        print(f"\n[!] לא נמצאו עובדים העונים לשם: {search_name}")
        conn.unbind()
        return

    print(f"\n[+] found: {len(conn.entries)}")
    print("=" * 60)
# מעבר על כל עובד שנמצא
    # מעבר על כל עובד שנמצא
    for user in conn.entries:
        # משיכת פרטי העובד (ללא היפוך שמות כדי למנוע טקסט הפוך בטרמינל)
        display_name = get_display(str(user.displayName))
        department = get_display(str(user.department))
        username = str(user.sAMAccountName)
        phone = user.telephoneNumber if user.telephoneNumber else "N/A"
        email = user.mail if user.mail else "N/A"

        # 1. הכנת בלוק הטקסט של פרטי העובד (ללא הדפסה עדיין)
        user_info = (
            f"[bold cyan]Username:[/bold cyan] {username}\n"
            f"[bold cyan]Department:[/bold cyan] {department}\n"
            f"[bold cyan]Phone:[/bold cyan] {phone}\n"
            f"[bold cyan]Email:[/bold cyan] {email}\n"
        )
        
        #  שלב ב': חיפוש המחשבים המשויכים לעובד
        computer_filter = f'(&(objectClass=computer)(name=*{username}*))'
        computer_attributes = ['name', 'operatingSystem', 'dNSHostName']
        
        conn.search(search_base=SEARCH_BASE, search_filter=computer_filter, attributes=computer_attributes)
        
        # בניית בסיס הטבלה מראש
        table = Table(show_header=True, header_style="bold magenta", border_style="bright_black")
        table.add_column("PC Name", style="dim", width=15)
        table.add_column("OS", width=20)
        table.add_column("IP Address", justify="center", width=15)
        table.add_column("Status", justify="center", width=15)

        if not conn.entries:
            # אם אין מחשבים, נשמור טקסט חלופי במקום הטבלה
            table_or_text = "[yellow]⚠ No computers ⚠[/yellow]"
        else:
            computers_to_check = []
            for pc in conn.entries:
                computers_to_check.append({
                    'name': str(pc.name),
                    'os': str(pc.operatingSystem),
                    'dns': str(pc.dNSHostName)
                })

            # הרצת בדיקות התקשורת
            with console.status(f"[bold green]בודק תקשורת ל-{len(computers_to_check)} מחשבים...", spinner="dots"):
                def check_pc_status(pc):
                    if pc['dns'] and pc['dns'] != 'None':
                        pc['is_online'] = ping_host(pc['dns'])
                        try:
                            pc['ip'] = socket.gethostbyname(pc['dns'])
                        except socket.gaierror:
                            pc['ip'] = "N/A"
                    else:
                        pc['is_online'] = None
                        pc['ip'] = "N/A"
                    return pc

                with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                    results = list(executor.map(check_pc_status, computers_to_check))

            # הכנסת הנתונים לתוך שורות הטבלה
            for pc in results:
                if pc['is_online'] is True:
                    status_str = "[bold green]ONLINE 🟢[/bold green]"
                elif pc['is_online'] is False:
                    status_str = "[bold red]OFFLINE 🔴[/bold red]"
                else:
                    status_str = "[bold white]UNKNOWN ⚪[/bold white]"
                
                table.add_row(pc['name'], pc['os'], pc['ip'], status_str)
            
            # אם יש מחשבים, המשתנה שלמטה יכיל את הטבלה המוכנה
            table_or_text = table

        # 3. חיבור הטקסט והטבלה לקבוצה אחת (Group) 
        user_group = Group(user_info, table_or_text)
        
        # 4. הדפסת מסגרת אחת בודדת שעוטפת את ה-Group
        console.print(Panel(user_group, title=f"👤 [bold white]{display_name}[/bold white]", border_style="blue", expand=False))
        console.print() # שורת רווח בין עובד לעובד

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <Employee_Name>")
        sys.exit(1)

    name_to_search = " ".join(sys.argv[1:])
    search_user_and_computer(name_to_search)