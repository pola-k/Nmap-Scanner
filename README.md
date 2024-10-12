# NMap Tool

## Overview
The NMap Tool is a simple Python application that automates network scanning using the NMap library. This tool allows users to perform various types of scans on specified IP addresses and provides valuable insights into open ports and the services running on them. It's designed for both novices and experienced users looking for an easy way to utilize NMap functionalities.

## Features
- **Automated Scan Selection**: Users can choose from different scan types (SYN ACK, UDP, Comprehensive) with a simple input.
- **Scan Information Retrieval**: Automatically gathers and displays results, including IP status, protocols used, and open ports.
- **User-Friendly Interface**: Prompts for necessary inputs, making it accessible for users unfamiliar with command-line operations.

## Technologies Used
- Python 3.x
- NMap library (`python-nmap`) for network scanning

## Getting Started

### Prerequisites
Make sure you have the following installed on your system:
- **Python 3.x**
- **NMap**: The network scanning tool
- **Nmap Python library (`python-nmap`)**

### Installation
1. **Install NMap**:
   - For Windows, download and install NMap from [nmap.org](https://nmap.org/download.html).
   - For Linux, you can usually install it via your package manager. For example:
     ```bash
     sudo apt install nmap
     ```

2. **Install the Python NMap library**:
   ```bash
   pip install python-nmap
   ```

3. **Clone the repository** (if applicable):
   ```bash
   git clone https://github.com/pola-k/Nmap-Scanner.git
   ```

4. **Change into the project directory** (if applicable):
   ```bash
   cd Nmap-Scanner
   ```

### Usage
1. Run the script:
   ```bash
   python nmap_scanner.py
   ```

2. When prompted, enter the IP address you wish to scan.

3. Choose the type of scan you want to conduct by entering the corresponding number:
   - **1** for SYN ACK Scan
   - **2** for UDP Scan
   - **3** for Comprehensive Scan

4. The results of the scan will be displayed, including:
   - Scan information
   - IP status
   - Protocols used
   - Open ports

### Example Output
```bash
Welcome, This is a Simple NMap Tool
NMap Version:  7.80
<--------------------------------------------->
Enter an IP Address you want to scan: 192.168.1.1

Enter the type of scan you want to run
1) SYN ACK Scan
2) UDP Scan
3) Comprehensive Scan
1
You want to conduct a SYN ACK Scan
...
IP Status:  up
Open TCP Ports:  [22, 80, 443]
```

## Limitations
- **NMap Installation**: Users must have NMap installed on their system for the tool to function.
- **Scan Customization**: The tool currently offers limited scan options. For custom scans, users will need to modify the script.
- **Error Handling**: The script includes basic error handling; invalid input or connectivity issues may not be handled comprehensively.

## Disclaimer
**Use this tool responsibly and only on networks you have permission to scan. Unauthorized scanning can be considered illegal and unethical.**
