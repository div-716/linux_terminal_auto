# How to Change Application Icon in Linux (RHEL 9)

## Steps:
1. Locate `.desktop` file:
   ```bash
   sudo find /usr/share/applications -name "*.desktop"
2. Open the file:
sudo nano /usr/share/applications/terminator.desktop

3. Edit the line:
Icon=/full/path/to/your/icon.png

4. Save and exit.

5. Restart GNOME Shell:
Alt + F2 → type `r` → press Enter

