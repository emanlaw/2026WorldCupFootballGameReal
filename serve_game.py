#!/usr/bin/env python3
import http.server
import ssl
import os

# Change to the directory containing this script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Create server
server_address = ('0.0.0.0', 8444)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
httpd.allow_reuse_address = True

# Wrap with SSL
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('server.pem')
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

import socket
import subprocess
import re

def get_local_ips():
    ips = []
    try:
        output = subprocess.check_output("ifconfig", shell=True).decode()
        matches = re.findall(r"inet (\d+\.\d+\.\d+\.\d+)", output)
        for ip in matches:
            if ip != "127.0.0.1":
                ips.append(ip)
    except:
        pass
    return ips

print(f"HTTPS Server running on port 8444")
local_ips = get_local_ips()
if local_ips:
    print("\n✅ Try these URLs on your iPhone:")
    for ip in local_ips:
        print(f"   https://{ip}:8444/3D%20Soccer%20Set-Piece%20Challenge.html")
else:
    print("   https://localhost:8444 (check your IP manually for mobile access)")

print("\n⚠️  SECURITY WARNING:")
print("   You will see a warning like 'Your connection is not private'.")
print("   Click 'Show Details' -> 'visit this website' (Safari) or 'Advanced' -> 'Proceed' (Chrome).")
print("   This is normal for a local self-signed certificate.")
print("\nPress Ctrl+C to stop")

httpd.serve_forever()
