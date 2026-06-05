
```markdown
<h1 align="center"> AD Help Desk CLI Tool</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Active%20Directory-LDAPS-success.svg" alt="AD LDAPS">
  <img src="https://img.shields.io/badge/UI-Rich-magenta.svg" alt="Rich UI">
</p>

<p align="center">
  <b>Advanced Command Line Interface (CLI) tool for system administrators and technical support to manage and investigate users and endpoints within the corporate network.</b>
</p>

---

## Features

* **Strict Security (LDAPS):** Encrypted connection to the Active Directory server via port 636 (TLS v1.2) to prevent packet sniffing.
* **Parallel Scanning (Multithreading):** Concurrent Ping tests and DNS resolution for all user endpoints simultaneously for instant results.
* **Visual User Interface (Rich UI):** Readable, modern, and colorful output based on the `Rich` library, featuring data tables and panels for quick visual orientation.
* **Full Hebrew Support:** Built-in adaptation for fetching, handling, and displaying Hebrew user names and departments (BiDi support).

---

## Installation

### Prerequisites
* Python 3.8 or higher.
* Physical or virtual access (VPN) to the corporate network (Domain Environment).

### Installation Steps
1. Clone the repository to your local environment:
   ```bash
   git clone [https://github.com/your-username/ad-helpdesk-cli.git](https://github.com/your-username/ad-helpdesk-cli.git)
   cd ad-helpdesk-cli

```

2. Create an isolated virtual environment (recommended):
```bash
python -m venv .venv

```


3. Activate the virtual environment:
* **Windows:**
```cmd
.venv\Scripts\activate

```


* **Mac/Linux:**
```bash
source .venv/bin/activate

```




4. Install dependencies from the requirements file:
```bash
pip install -r requirements.txt

```



---

## Configuration

The project uses environment variables to protect sysadmin credentials. **Never store passwords in the source code.**

Create a new file named `.env` in the project root directory and enter the following details according to your infrastructure:

```env
# Active Directory Server Settings
AD_SERVER=
AD_SEARCH_BASE=DC=

# Sysadmin Credentials (Read permissions required in AD)
AD_USER=MUNICIPALITY\YourUsername
AD_PASSWORD=YourSecretPassword

```
---

## Usage

Run the script by passing the employee's name (or a keyword from their name) as a command-line argument. You can enter just a first name or a full name.

**Basic Syntax:**

```bash
python main.py <Employee_Name>

```

**Run Examples:**

```bash
python main.py Daniel
python main.py Rachel Berman

```

### Output Example

Upon execution, the script will:

1. Locate the user and display their details in a structured panel (Name, Username, Department, Phone, Email).
2. Scan to find all computers registered under the user in AD (e.g., `PC-DANIEL` or `NB-DANIEL`).
3. Print a real-time table showing the OS version, IP address, and availability status (ONLINE 🟢 / OFFLINE 🔴).

---

## 🛠️ Dependencies

* [ldap3](https://ldap3.readthedocs.io/) - Communication with the Active Directory server.
* [rich](https://rich.readthedocs.io/) - Terminal formatting (tables, panels, statuses).
* [python-dotenv](https://pypi.org/project/python-dotenv/) - Secure environment variable management.
* [python-bidi](https://pypi.org/project/python-bidi/) - Algorithm for Hebrew text alignment (BiDi).

```

```