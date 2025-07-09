port-scan-detector/
├── scan_detector.py         ✅ Main Python script
├── suspicious_hosts.txt     ✅ Output: list of flagged IPs
├── logs/scan_log.txt        ✅ Output: full scan log
├── config.json              ✅ Settings (thresholds, network range)
├── README.md                ✅ Project documentation
└── requirements.txt         ✅ Required packages


# Port Scan Detector 🔍

A beginner-friendly Python tool to detect suspicious network scanning activity using `nmap`.

## 📌 Features
- Runs automated scans using `nmap`
- Logs scan results with timestamps
- Flags suspicious activity based on host count
- Configurable via `config.json`

## 🛠 Requirements
- Python 3
- `nmap` installed and accessible via command line

## 🚀 Getting Started

```bash
git clone https://github.com/yourusername/port-scan-detector.git
cd port-scan-detector
python3 scan_detector.py
