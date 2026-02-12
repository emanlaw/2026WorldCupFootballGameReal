# Web Export Build

This folder contains the exported web version of the game for testing on mobile devices.

## Quick Start

### 1. Export from Godot
```
Project → Export → Web → Export Project
```
**IMPORTANT**: Thread Support must be DISABLED for iOS Safari!

### 2. Start Server
```bash
cd build/web
python3 serve_game.py
```

### 3. Test on iPhone
Open Safari and go to:
```
http://YOUR_COMPUTER_IP:8000/3D%20Soccer%20Set-Piece%20Challenge.html
```

Find your IP: `ifconfig | grep "inet " | grep -v 127.0.0.1`

## Current Configuration

✅ **Thread Support**: DISABLED (iOS compatible)  
✅ **Orientation**: Portrait  
✅ **Canvas Resize**: Adaptive  
✅ **Export Path**: Configured

## Testing Checklist

- [ ] Game loads on iPhone Safari
- [ ] Touch/swipe input works
- [ ] Ball curves correctly
- [ ] Performance is smooth
- [ ] Portrait orientation correct

## Need Help?

See detailed guide: `docs/WEB_EXPORT_GUIDE.md`

## Files

- `*.html` - Main game file
- `*.js` - Game code
- `*.wasm` - WebAssembly binary
- `*.pck` - Game assets
- `serve_game.py` - Local test server
