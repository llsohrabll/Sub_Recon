import ipaddress
import subprocess
from termcolor import colored

def ping_ip(ip):
    """Ping an IP address and return True if reachable, False otherwise."""
    result = subprocess.run(["ping", "-c", "1", "-W", "1", str(ip)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0

def get_host(ip):
    """Get the hostname of an IP address using the host command."""
    try:
        result = subprocess.run(["host", str(ip)], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error retrieving host: {e}"

def scan_network(cidr):
    """Scan a given CIDR range, ping each IP, and get its hostname, then save results to output.txt."""
    network = ipaddress.ip_network(cidr, strict=False)
    
    with open("output.txt", "w") as file:
        for ip in network.hosts():  
            reachable = ping_ip(ip)
            host_info = get_host(ip)
            
            if reachable and "not found" not in host_info:
                result = f"{colored(ip, 'green')} is {colored('reachable', 'green')} | {colored(host_info, 'blue')}\n"
            elif not reachable and "not found" in host_info:
                result = f"{colored(ip, 'red')} is {colored('not reachable', 'red')} | {colored(host_info, 'red')}\n"
            else:
                result = f"{ip} is {'reachable' if reachable else 'not reachable'} | {host_info}\n"
            
            print(result, end="")  
            file.write(result) 

if __name__ == "__main__":
    cidr_input = input("Enter CIDR range (e.g., 192.168.1.0/24): ")
    scan_network(cidr_input)
