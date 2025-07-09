import subprocess
import time
import json
from datetime import datetime

CONFIG_FILE = 'config.json'
LOG_FILE = 'logs/scan_log.txt'
SUSPICIOUS_FILE = 'suspicious_hosts.txt'

def load_config():
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)

def run_nmap_scan(network_range):
    result = subprocess.run(['nmap', '-sP', network_range], capture_output=True, text=True)
    return result.stdout

def log_scan_output(output):
    with open(LOG_FILE, 'a') as f:
        f.write(f"\n--- Scan at {datetime.now()} ---\n")
        f.write(output)

def detect_suspicious(output, threshold):
    hosts = [line for line in output.split('\n') if "Nmap scan report for" in line]
    if len(hosts) > threshold:
        with open(SUSPICIOUS_FILE, 'a') as f:
            f.write(f"Suspicious activity at {datetime.now()} - {len(hosts)} hosts detected\n")
        print("⚠️ Suspicious activity detected!")
    else:
        print("✅ No suspicious activity.")

def main():
    config = load_config()
    while True:
        print(f"🔍 Scanning {config['network_range']}...")
        output = run_nmap_scan(config['network_range'])
        log_scan_output(output)
        detect_suspicious(output, config['threshold'])
        print(f"Waiting {config['scan_interval']} seconds for next scan...\n")
        time.sleep(config['scan_interval'])

if __name__ == "__main__":
    main()
