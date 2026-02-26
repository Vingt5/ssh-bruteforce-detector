![Python](https://img.shields.io/badge/Python-3.x-blue)
![Security](https://img.shields.io/badge/Focus-Blue%20Team-blue)
![Status](https://img.shields.io/badge/Project-Active-success)

# 🚨 SSH Brute Force Detector

Detect brute-force SSH login attempts from Linux authentication logs.

---

## 🔍 Overview

This tool analyzes SSH authentication logs and identifies suspicious IP addresses based on repeated failed login attempts.

Brute-force attacks remain one of the most common intrusion techniques used to gain unauthorized access.  
This script helps detect early signs of such attacks by monitoring failed SSH login attempts.

---

## ⚙️ Features

- Detect failed SSH login attempts  
- Count repeated attempts per IP address  
- Highlight suspicious IPs based on a configurable threshold  
- Lightweight and easy to use  
- Useful for SOC monitoring & security labs  

---

## 🛠️ How It Works

The script scans log entries for failed SSH login attempts and counts how many times each IP address appears.

Example log entry detected:

Failed password for invalid user admin from 192.168.1.10

When an IP exceeds the threshold (default: **3 attempts**), it is flagged as suspicious.

---

## 📦 Project Structure

ssh-bruteforce-detector/
- detector.py        → detection script  
- sample_log.txt     → sample log for testing  
- README.md  

---

## ▶️ Usage

Run the script:

python detector.py

---

## 🧪 Example Output

Suspicious IPs:

192.168.1.10 → 3 failed attempts

---

## 🎯 Why This Matters

Monitoring authentication logs helps detect:

- brute-force attacks  
- credential stuffing attempts  
- unauthorized access attempts  
- early signs of compromise  

This type of detection is a fundamental task in **Security Operations Centers (SOC)** and Blue Team activities.

---

## 🧪 Real-World Use Case

This script can help detect:

- SSH brute-force attempts
- credential stuffing attacks
- unauthorized access attempts
- early compromise indicators

---

## 🚀 Possible Improvements

- real-time log monitoring  
- configurable thresholds  
- automatic IP blocking (fail2ban-style)  
- CSV/JSON export  
- email or SIEM alerting  

---

## 👨‍💻 Author

Cybersecurity student focused on:

- Blue Team operations  
- Threat detection & incident response  
- Security monitoring & log analysis  

---

## 📜 License

This project is open-source and available for educational and security research purposes.
