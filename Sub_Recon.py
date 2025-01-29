import subprocess
import os
import time
import json
import xml.etree.ElementTree as ET
from typing import Set
import sys

if len(sys.argv) < 5 or sys.argv[1] != '-d' or sys.argv[3] != '-w' or sys.argv[5] != '-r':
    print("Usage: python3 Sub_Recon.py -d <domain> -w <wordlist.txt> -r <resolver.txt>")
    sys.exit(1)

domain = sys.argv[2]
wordlist = sys.argv[4]
resolvers = sys.argv[6]

required_tools = [
    "subfinder",
    "sublist3r",
    "amass",
    "assetfinder",
    "findomain",
    "dnsrecon",
    "gobuster",
    "theharvester"
]

def install_required_tools():
    for tool in required_tools:
        try:
            subprocess.run(["which", tool], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"[+] {tool} is already installed.")
        except subprocess.CalledProcessError:
            print(f"[-] {tool} not found. Installing {tool}...")
            subprocess.run(["sudo", "apt", "install", "-y", tool], check=True)

class SubdomainScanner:
    def __init__(self, domain: str, wordlist: str, resolvers: str):
        self.domain = domain
        self.subdomains: Set[str] = set()
        self.report_dir = f"subdomain_reports_{self.domain}"
        self.wordlist = wordlist
        self.resolvers = resolvers
        
        os.makedirs(self.report_dir, exist_ok=True)

    def run_sublist3r(self):
        try:
            output_file = f"{self.report_dir}/sublist3r.txt"
            subprocess.run([
                "sublist3r",
                "-d", self.domain,
                "-o", output_file
            ], check=True)
            
            with open(output_file, "r") as f:
                self.subdomains.update(line.strip() for line in f if line.strip())
                
        except Exception as e:
            print(f"[!] Sublist3r error: {str(e)}")

    def run_subfinder(self):
        try:
            output_file = f"{self.report_dir}/subfinder.txt"
            subprocess.run([
                "subfinder",
                "-d", self.domain,
                "-o", output_file
            ], check=True)
            
            with open(output_file, "r") as f:
                self.subdomains.update(line.strip() for line in f if line.strip())
                
        except Exception as e:
            print(f"[!] Subfinder error: {str(e)}")

    def run_amass(self):
        try:
            output_file = f"{self.report_dir}/amass.txt"
            subprocess.run([
                "amass",
                "enum",
                "-d", self.domain,
                "-o", output_file
            ], check=True)
            
            with open(output_file, "r") as f:
                self.subdomains.update(line.strip() for line in f if line.strip())
                
        except Exception as e:
            print(f"[!] Amass error: {str(e)}")

    def run_assetfinder(self):
        try:
            result = subprocess.check_output([
                "assetfinder",
                "--subs-only",
                self.domain
            ]).decode("utf-8")
            
            self.subdomains.update(result.splitlines())
            
        except Exception as e:
            print(f"[!] Assetfinder error: {str(e)}")

    def run_findomain(self):
        try:
            output_file = f"{self.report_dir}/findomain.txt"
            subprocess.run([
                "findomain",
                "-t", self.domain,
                "-o"
            ], check=True)
            
            temp_file = f"{self.domain}.txt"
            if os.path.exists(temp_file):
                os.rename(temp_file, output_file)
                
            with open(output_file, "r") as f:
                self.subdomains.update(line.strip() for line in f if line.strip())
                
        except Exception as e:
            print(f"[!] Findomain error: {str(e)}")

    def run_dnsrecon(self):
        try:
            xml_output = f"{self.report_dir}/dnsrecon.xml"
            subprocess.run([
                "dnsrecon",
                "-d", self.domain,
                "-x", xml_output
            ], check=True)
            
            tree = ET.parse(xml_output)
            root = tree.getroot()
            
            for record in root.findall(".//record"):
                if record.get('type') in ['A', 'CNAME']:
                    name = record.get('name')
                    if name:
                        self.subdomains.add(name.strip().lower())
                        
        except Exception as e:
            print(f"[!] DNSrecon error: {str(e)}")

    def run_gobuster(self):
        try:
            result = subprocess.check_output([
                "gobuster",
                "dns",
                "-d", self.domain,
                "-w", self.wordlist,
                "-q"
            ]).decode("utf-8")
            
            for line in result.splitlines():
                if "Found: " in line:
                    self.subdomains.add(line.split(" ")[1])
                    
        except Exception as e:
            print(f"[!] Gobuster error: {str(e)}")

    def run_theharvester(self):
        try:
            output_file = f"{self.report_dir}/theharvester.xml"
            subprocess.run([
                "theHarvester",
                "-d", self.domain,
                "-b", "all",
                "-f", output_file
            ], check=True)
            
            tree = ET.parse(f"{output_file}.xml")
            root = tree.getroot()
            
            for host in root.findall(".//host"):
                hostname = host.get('name')
                if hostname:
                    self.subdomains.add(hostname.strip().lower())
                    
        except Exception as e:
            print(f"[!] theHarvester error: {str(e)}")

    def run_all_tools(self):
        tools = [
            self.run_sublist3r,
            self.run_subfinder, 
            self.run_amass,
            self.run_assetfinder,
            self.run_findomain,
            self.run_dnsrecon,
            self.run_gobuster,
            self.run_theharvester
        ]
        
        print(f"[*] Starting subdomain enumeration for {self.domain}")
        for tool in tools:
            print(f"[+] Running {tool.__name__}...")
            start_time = time.time()
            tool()
            elapsed = time.time() - start_time
            print(f"    Completed in {elapsed:.2f} seconds")
        
        final_file = f"{self.report_dir}/all_subdomains.txt"
        with open(final_file, "w") as f:
            f.write("\n".join(sorted(self.subdomains)))
            
        print(f"\n[+] Found {len(self.subdomains)} unique subdomains")
        print(f"[*] Results saved to: {final_file}")

if __name__ == "__main__":
    install_required_tools()

    scanner = SubdomainScanner(domain, wordlist, resolvers)
    scanner.run_all_tools()
