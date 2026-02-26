import re
from collections import defaultdict

log_file = "sample_log.txt"

pattern = re.compile(r"Failed password.*from (\d+\.\d+\.\d+\.\d+)")

attempts = defaultdict(int)

with open(log_file, "r") as file:
    for line in file:
        match = pattern.search(line)
        if match:
            ip = match.group(1)
            attempts[ip] += 1

print("\nSuspicious IPs:\n")

for ip, count in attempts.items():
    if count >= 3:
        print(f"{ip} → {count} failed attempts")
