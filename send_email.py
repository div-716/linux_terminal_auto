#### 📄 `send_email.py`
```python
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Test Mail from Linux Terminal'
msg['From'] = 'your_email@gmail.com'
msg['To'] = 'receiver_email@gmail.com'
msg.set_content('Hi, this is a test email sent from Python in Linux Terminal.')

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login('your_email@gmail.com', 'your_app_password')  # use app password
server.send_message(msg)
server.quit()
