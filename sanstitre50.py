# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 04:55:23 2024

@author: pc
"""

import re

# Journaux réseau fictifs
logs = [
    "192.168.1.10 - OK",
    "172.16.0.1 - Anomaly detected",
    "10.0.0.5 - OK",
    "203.0.113.5 - Suspicious activity"
]

# Règles simples : détection d'adresses IP publiques
def is_suspicious_ip(ip):
    private_ranges = [
        re.compile(r'^192\.168\.'),  # Plage privée 192.168.x.x
        re.compile(r'^10\.'),       # Plage privée 10.x.x.x
        re.compile(r'^172\.16\.')   # Plage privée 172.16.x.x
    ]
    return not any(rule.match(ip) for rule in private_ranges)

for log in logs:
    ip = log.split(" - ")[0]
    if is_suspicious_ip(ip):
        print(f"Adresse IP suspecte détectée : {ip}")
