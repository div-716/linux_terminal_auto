from twilio.rest import Client

# Replace with your actual credentials
account_sid = 'your_twilio_account_sid'
auth_token = 'your_twilio_auth_token'

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello from Linux Terminal via Python!",
    from_='+1xxxxxxxxxx',     # Twilio phone number
    to='+91xxxxxxxxxx'        # Your personal number
)

print(f"Message sent with SID: {message.sid}")
