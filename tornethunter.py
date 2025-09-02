"""
TorNetHunter - Menu driven CLI entrypoint
"""
import os
import sys
import time
from modules import recon, scan, brute, tunnel, utils

LOG_DIR = os.path.expanduser("~/TorNetHunter/logs")
os.makedirs(LOG_DIR, exist_ok=True)

BANNER = r"""
████████╗ ██████╗ ██████╗ ███╗   ██╗███████╗████████╗██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ 
╚══██╔══╝██╔═══██╗██╔══██╗████╗  ██║██╔════╝╚══██╔══╝██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
   ██║   ██║   ██║██████╔╝██╔██╗ ██║█████╗     ██║   ███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
   ██║   ██║   ██║██╔═══╝ ██║╚██╗██║██╔══╝     ██║   ██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
   ██║   ╚██████╔╝██║     ██║ ╚████║███████╗   ██║   ██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
   ╚═╝    ╚═════╝ ╚═╝     ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                         🔥 TorNetHunter - Anonymous Pentesting Framework 🔥
"""
def menu():
    while True:
        os.system("clear")
        print(BANNER)
    
def pause():
    input("\nPress Enter to continue...")

def menu():
    while True:
        os.system("clear")
        print(BANNER)
        print("[1] Subdomain Enumeration (Onion-Recon)")
        print("[2] Brute Force Attack (Onion-Brute)  *Requires explicit permission*")
        print("[3] Port Scanning (Onion-Scan)")
        print("[4] Whois & DNS Recon (Onion-Intel)")
        print("[5] Dark Web Crawler (Onion-Crawl)  (.onion targets)")
        print("[6] Anonymity Check (Onion-Check)")
        print("[0] Exit\n")
        choice = input("Select an option: ").strip()

        if choice == "1":
            recon.run_interactive()
            pause()
        elif choice == "2":
            brute.run_interactive()
            pause()
        elif choice == "3":
            scan.run_interactive()
            pause()
        elif choice == "4":
            recon.intel_interactive()
            pause()
        elif choice == "5":
            recon.crawl_interactive()
            pause()
        elif choice == "6":
            utils.check_tor_interactive()
            pause()
        elif choice == "0":
            print("\n[+] Exiting TorNetHunter. Stay ethical & anonymous!")
            sys.exit(0)
        else:
            print("[-] Invalid option, try again.")
            time.sleep(1)

if __name__ == "__main__":
    try:
        
        utils.ensure_tor_started()
        utils.rotate_tor()
    except Exception as e:
        print(f"[!] Warning during Tor setup: {e}")
    menu()
