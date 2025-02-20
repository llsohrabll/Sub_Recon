Range IP Scanner
==============

This Python script scans a given CIDR range, pings each IP address, retrieves its hostname, 
and logs the results in output.txt.

Features:
---------
- Pings all IPs in the specified CIDR range
- Retrieves hostname information using the "host" command
- Displays results in the terminal with color-coded output
- Saves results to "output.txt"

Requirements:
-------------
Make sure you have Python installed on your system. You also need to install the required dependencies:

pip install termcolor

Usage:
------
1. Clone or download this script to your local machine.
2. Open a terminal and navigate to the script's directory.
3. Run the script:

   python3 scanner.py

4. Enter a valid CIDR range when prompted, for example:
   ```bash
   Enter CIDR range (e.g., 192.168.1.0/24): 192.168.1.0/24

6. The script will scan the network and display results in the terminal while saving them to "output.txt".

Output Example:
---------------
192.168.1.1 is reachable | Host: router.local
192.168.1.2 is not reachable | Host not found
192.168.1.3 is reachable | Host: printer.office

Notes:
------
- The script uses the "ping" and "host" commands, which must be available on your system.
- Run the script with appropriate permissions to access the network.
- The script is designed for Linux/macOS. On Windows, modify the "ping" command (-n instead of -c).
