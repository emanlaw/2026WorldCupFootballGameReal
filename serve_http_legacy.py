#!/usr/bin/env python3
"""
Simple HTTP server for Godot Web exports (iOS Safari compatible)
Thread support DISABLED - no special headers needed
"""
import http.server
import socketserver

class SimpleRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Basic CORS header for local testing
        self.send_header('Access-Control-Allow-Origin', '*')
        # Strong cache control - force reload every time
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

PORT = 8000

print("=" * 60)
print("🎮 Godot Web Game Server (iOS Safari Compatible)")
print("=" * 60)
import socket

def get_local_ips():
    ips = []
    try:
        # Get all network interfaces
        import subprocess
        import re
        output = subprocess.check_output("ifconfig", shell=True).decode()
        # Find all IPs (simple regex for IPv4)
        matches = re.findall(r"inet (\d+\.\d+\.\d+\.\d+)", output)
        for ip in matches:
            if ip != "127.0.0.1":
                ips.append(ip)
    except Exception as e:
        print(f"Could not detect IPs: {e}")
    return ips

print(f"\n✅ Server starting on port {PORT}...")
local_ips = get_local_ips()
if local_ips:
    print("\n📱 Try these URLs on your iPhone (ensure same Wi-Fi):")
    for ip in local_ips:
        print(f"   http://{ip}:{PORT}/3D%20Soccer%20Set-Piece%20Challenge.html")
else:
    print("\n⚠️  Could not detect local IP. Check 'ifconfig' manually.")
    
print("\n💡 Thread support is DISABLED for iOS compatibility")
print("   No special headers required!")
print("\n⏹️  Press Ctrl+C to stop the server")
print("=" * 60)
print()

Handler = SimpleRequestHandler
with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped")
