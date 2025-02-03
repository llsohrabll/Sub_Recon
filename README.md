# Sub_Recon

A simple tool to perform domain-related reconnaissance using various tools.

## Developed by
Sohrab Kaghazian

## Tools Used
This script utilizes the following reconnaissance tools:

- **Sublist3r**: A fast subdomain enumeration tool for penetration testers.
- **Subfinder**: A tool for discovering subdomains using passive sources.
- **Amass**: A powerful open-source tool for network mapping of attack surfaces and external assets.
- **Assetfinder**: A tool to find assets related to a given domain.
- **Findomain**: A fast subdomain discovery tool that supports different sources.
- **Dnsrecon**: A DNS reconnaissance tool to gather information about domains.
- **Gobuster**: A tool for directory and subdomain busting.
- **TheHarvester**: A tool for gathering information from public sources such as search engines.

## Usage

1. Install Python 3 if you haven't already. You can download it from the official website: [Python Downloads](https://www.python.org/downloads/).
   or
   
   ```bash
   sudo apt update
   ```
   ```bash
   sudo apt install python3
   ```
   ```bash
   python3 --version
   ```
3. Run the tool with the following command:

   ```bash
   python3 Sub_Recon.py -d <domain> -w <wordlist.txt> -r <resolver.txt>

- ***Note***: All Packeages are Installed Automatically or Updated if alreadt exist !
