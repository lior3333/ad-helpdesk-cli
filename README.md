
```markdown
<div align="center">

# AD Help Desk CLI Tool

**Advanced Command Line Interface (CLI) tool for system administrators and technical support to manage and investigate users and endpoints within the corporate network.**

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Active Directory](https://img.shields.io/badge/Active%20Directory-LDAPS-success.svg?style=for-the-badge&logo=windows&logoColor=white)]()
[![UI](https://img.shields.io/badge/UI-Rich-magenta.svg?style=for-the-badge)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

<img src="https://via.placeholder.com/800x400.png?text=+[Insert+Terminal+GIF/Screenshot+Here]+" alt="CLI Demo" width="100%">

</div>

---

<details>
  <summary><b>Table of Contents</b> (Click to expand)</summary>
  
  - [Features](#features)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Usage](#usage)
  - [Dependencies](#dependencies)
  - [Contributing](#contributing)
  - [License](#license)
</details>

---

## Features

- **Strict Security (LDAPS)**
  Encrypted connection to the Active Directory server via port 636 (TLS v1.2) to prevent packet sniffing and credential theft.
- **Parallel Scanning (Multithreading)**
  Concurrent Ping tests and DNS resolution for all user endpoints simultaneously, delivering instant diagnostic results.
- **Visual User Interface (Rich UI)**
  Readable, modern, and colorful output based on the `Rich` library, featuring data tables and panels for quick visual orientation.
- **Full Hebrew Support (BiDi)**
  Built-in adaptation for fetching, handling, and displaying right-to-left Hebrew user names and departments natively in the terminal.

---

## Installation

### Prerequisites

Ensure you have the following before starting:
- **Python:** Version 3.8 or higher.
- **Network:** Physical or virtual access (VPN) to the corporate Domain Environment.

### Setup Guide

**1. Clone the repository:**
```bash
git clone [https://github.com/lior3333/ad-helpdesk-cli.git]
cd ad-helpdesk-cli

```

**2. Create an isolated virtual environment:**

```bash
python -m venv .venv

```

**3. Activate the virtual environment:**

* **Windows:**
```cmd
.venv\Scripts\activate

```


* **Mac/Linux:**
```bash
source .venv/bin/activate

```



**4. Install dependencies:**

```bash
pip install -r requirements.txt

```

---

## Configuration

> [!WARNING]
> **Critical Security Notice:** This project uses environment variables to protect sysadmin credentials. Never commit passwords or `.env` files to version control. Ensure `.env` is listed in your `.gitignore`.

Create a file named `.env` in the root directory of the project and populate it with your environment details:

```env
# Active Directory Server Settings
AD_SERVER=192.168.1.100
AD_SEARCH_BASE=DC=company,DC=com

# Sysadmin Credentials (Read permissions required)
AD_USER=DOMAIN\AdminUser
AD_PASSWORD=YourSecretPassword

```

---

## Usage

Run the script by passing the employee's name (or a keyword from their name) as a command-line argument. The tool supports partial and full names.

**Basic Syntax:**

```bash
python main.py <Employee_Name>

```

**Examples:**

```bash
python main.py John
python main.py Jane Doe

```

### Output Example

Upon execution, the script performs the following workflow:

1. **Locate & Display:** Fetches the user and displays details in a structured panel (Name, Username, Department, Phone, Email).
2. **Endpoint Discovery:** Scans AD for all computer objects associated with the user.
3. **Live Diagnostics:** Prints a real-time table showing the OS version, resolved IP address, and availability status (`[ONLINE]` / `[OFFLINE]`).

---

## Dependencies

This project relies on the following open-source libraries:

| Library | Description |
| --- | --- |
| [`ldap3`](https://ldap3.readthedocs.io/) | Pure Python strictly RFC 4510 conforming LDAP V3 client. |
| [`rich`](https://rich.readthedocs.io/) | Library for rich text and beautiful formatting in the terminal. |
| [`python-dotenv`](https://pypi.org/project/python-dotenv/) | Reads key-value pairs from a `.env` file and sets them as environment variables. |
| [`python-bidi`](https://pypi.org/project/python-bidi/) | Pure Python implementation of the BiDi layout algorithm. |

---

## Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check the [issues page](https://www.google.com/search?q=https://github.com/your-username/ad-helpdesk-cli/issues) if you want to contribute.

## License

Distributed under the MIT License. See `LICENSE` for more information.

```

```