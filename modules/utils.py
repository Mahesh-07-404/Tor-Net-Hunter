import socket
import subprocess
import time
from stem import Signal
from stem.control import Controller

TOR_SOCKS_HOST = "127.0.0.1"
TOR_SOCKS_PORT = 9050
TOR_CONTROL_PORT = 9051

def is_tor_listening():
    s = socket.socket()
    try:
        s.settimeout(2)
        s.connect((TOR_SOCKS_HOST, TOR_SOCKS_PORT))
        return True
    except Exception:
        return False
    finally:
        try:
            s.close()
        except:
            pass

def ensure_tor_started():
    if is_tor_listening():
        print("[*] Tor is already running.")
        return
    print("[*] Tor not detected. Attempting to start Tor service (requires sudo)...")
    try:
        subprocess.run(["sudo", "systemctl", "start", "tor"], check=True)
        time.sleep(2)
        if not is_tor_listening():
            raise RuntimeError("Tor service didn't start or is not listening on 127.0.0.1:9050")
        print("[*] Tor started.")
    except Exception as e:
        raise RuntimeError(f"Failed to start Tor: {e}")

def rotate_tor():
    try:
        with Controller.from_port(port=TOR_CONTROL_PORT) as controller:
            controller.authenticate()  # cookie auth by default on many systems
            controller.signal(Signal.NEWNYM)
            print("[*] Tor NEWNYM signal sent (rotated identity).")
    except Exception as e:
        print(f"[!] Could not rotate Tor identity: {e}")

def check_exit_ip_via_tor():
    import requests
    proxies = {"http": f"socks5h://{TOR_SOCKS_HOST}:{TOR_SOCKS_PORT}",
               "https": f"socks5h://{TOR_SOCKS_HOST}:{TOR_SOCKS_PORT}"}
    try:
        r = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=15)
        return r.json().get("origin", "")
    except Exception as e:
        return f"Error: {e}"

def check_tor_interactive():
    print("[*] Checking Tor connectivity and exit IP via Tor...")
    if not is_tor_listening():
        print("[-] Tor does not seem to be running.")
        return
    ip = check_exit_ip_via_tor()
    print(f"[+] Tor exit IP: {ip}")
