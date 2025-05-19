import os
import time

print("[*] Simulating CPU-intensive malicious activity using stress...")

# Check if 'stress' is installed
if os.system("which stress > /dev/null") != 0:
    print("[!] 'stress' not found. Installing it now...")
    os.system("sudo apt update && sudo apt install -y stress")

# Run the stress command for 100 seconds
try:
    duration = 2050
    print(f"[*] Running: stress --cpu 4 --timeout {duration}")
    os.system(f"stress --cpu 4 --timeout {duration}")
    print("[+] Malicious CPU stress simulation completed.")
except KeyboardInterrupt:
    print("[!] Interrupted by user.")

