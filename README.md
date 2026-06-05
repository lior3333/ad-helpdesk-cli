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
git clone [https://github.com/lior3333/ad-helpdesk-cli.git](https://github.com/lior3333/ad-helpdesk-cli.git)
cd ad-helpdesk-cli