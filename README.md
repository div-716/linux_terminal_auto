1. { gui_programs_and_commands} :

Description: List of 5 popular GUI programs in Linux and the terminal commands that launch them.

Programs Covered:

Nautilus (nautilus)

Gedit (gedit)

Firefox (firefox)

LibreOffice Writer (libreoffice --writer)

GNOME Terminal (gnome-terminal)

Tips:

Run from Alt+F2 or CLI.

Check installation using which or dnf list installed.

-------------------------------------------------------------------------------------------------------------------------------------------------
2. { change_app_icon} :

Description: Demonstrates how to change the logo/icon of a Linux application (e.g., Terminator).

Requirements:

.png icon file

Edit .desktop entry file, usually in /usr/share/applications/

Tips:

Make sure the new icon path is absolute.

Restart GNOME shell (Alt+F2 → r) or reboot if not visible.
___________________________________________________________________________________________________________________________________________________

3. { add_more_terminals_gui } :

Description: Instructions for installing new terminals (like terminator) and GUI enhancements in RHEL 9.

Includes:

Source build steps for Terminator.

.desktop launcher creation.

Tips:

Install dependencies first: pip install configobj

If GNOME Shell doesn’t refresh, restart system or use Alt+F2 > r
____________________________________________________________________________________________________________________________________________________

4. { send_email_whatsapp_tweet_sms/} :

Description: Scripts to send communication messages via terminal.

Requirements:

> Python 3.x

> Internet access

pip install:

> smtplib (builtin)

> twilio

> selenium

> tweepy

Scripts:

> send_email.py: Send email via Gmail SMTP.

> send_whatsapp.py: Send WhatsApp message via Selenium automation.

> send_sms.py: Use Twilio API.

> send_tweet.py: Post tweet using Tweepy and Twitter API.

Tips:

> Use environment variables for credentials.

> For WhatsApp, scan QR code during first run.

_______________________________________________________________________________________________________________________________________________

{ ctrl_c_ctrl_z_commands } :

Description: Investigation of interrupt signals (Ctrl+C and Ctrl+Z).

Commands:

Ctrl+C sends SIGINT (killable)

Ctrl+Z sends SIGTSTP (suspend)

View with: stty -a or kill -l

Tips:

Use jobs, bg, fg, and kill for process control.

Practice with long-running scripts like sleep 100

_______________________________________________________________________________________________________________________________________________

How to Run All Python Scripts:

cd folder_name
python3 script_name.py

Ensure dependencies are installed for each script using:
pip install -r requirements.txt

______________________________________________________________________________________________________________________________________________

Blog on linux : [ https://medium.com/@sdivyanshi573/the-rapid-rise-of-linux-gaining-popularity-in-companies-4a9132f4dc46 ]
