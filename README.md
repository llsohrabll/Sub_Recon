# 🕵️‍♂️ **Sub_Recon** 🕵️‍♀️

A simple tool to perform domain-related reconnaissance using various tools. 🌐🔍

## 👨‍💻 **Developed by**
**Sohrab Kaghazian** 

## 🛠️ **Tools Used**

This script utilizes the following reconnaissance tools:

- **🔑 Sublist3r**: A fast subdomain enumeration tool for penetration testers.
- **🕵️‍♂️ Subfinder**: A tool for discovering subdomains using passive sources.
- **⚡ Amass**: A powerful open-source tool for network mapping of attack surfaces and external assets.
- **🔍 Assetfinder**: A tool to find assets related to a given domain.
- **🚀 Findomain**: A fast subdomain discovery tool that supports multiple passive sources.
- **📡 Dnsrecon**: A DNS reconnaissance tool to gather DNS-related information about domains.
- **📂 Gobuster**: A tool for directory and subdomain busting using wordlist-based brute-forcing.
- **🧑‍💻 TheHarvester**: A tool for gathering information from public sources such as search engines, social media, and more.
- **🔨 Knockpy**: A subdomain brute-force tool that uses a wordlist to find subdomains for a given domain.

## ✨ **Features**

- **⚙️ Automatic Tool Installation & Update**: All required tools are automatically installed if missing and updated if already present.
- **🔍 Comprehensive Subdomain Enumeration**: Supports multiple tools for subdomain discovery and DNS reconnaissance.
- **💡 Easy-to-Use Command-Line Interface**: Just run a simple command and get the results!

## 🛠️ **Installation Instructions**

1. **🔹 Install Python 3** (if you haven't already):

   - Download it from the official website: [Python Downloads](https://www.python.org/downloads/). 🌐
   - Alternatively, run the following commands to install it on Linux-based systems (Ubuntu/Debian):

   ```bash
   sudo apt update
   sudo apt install python3
   python3 --version
   ```

2. **🔹 Clone the Repository** (if you haven't already):

   ```bash
   git clone https://github.com/llsohrabll/Sub_Recon.git
   cd Sub_Recon

3. **🔹 Usage:

   ```bash
   python3 Sub_Recon.py -d <domain> -w <wordlist.txt> -r <resolver.txt>
