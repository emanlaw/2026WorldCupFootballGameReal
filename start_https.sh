#!/bin/bash
echo "Starting HTTPS server on port 8444..."
echo ""
echo "Access the game on your iPhone at:"
echo "  https://192.168.10.33:8444/3D%20Soccer%20Set-Piece%20Challenge.html"
echo ""
echo "Note: You'll see a security warning - tap 'Advanced' then 'Proceed'"
echo "Press Ctrl+C to stop"
echo ""

python3 -m http.server 8444 --bind 0.0.0.0 &
SERVER_PID=$!

# Wait a bit for server to start
sleep 1

echo "Server started (PID: $SERVER_PID)"
echo ""
echo "Setting up SSL proxy..."

# Keep running
wait $SERVER_PID
