#!/usr/bin/python3

import requests
import re

URL = "https://www.abuseipdb.com/sitemap?page="

ip_pattern = 'href="https://www.abuseipdb.com/check/(.+)"'
malicious = []

for ip in range(1,195):
    
    r = requests.get(url=URL+str(ip)).text
    if re.findall(pattern=ip_pattern, string=r):
        malicious.append(re.findall(pattern=ip_pattern, string=r))
    break
with open('malicious-ips.txt', 'w') as file:
    for i in malicious:
        file.writelines('\n'.join(i))

# Sort the output on this site:
# https://www.ipvoid.com/sort-ip-addresses/