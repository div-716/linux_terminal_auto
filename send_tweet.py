import tweepy

# Replace with your actual credentials
api_key = 'your_api_key'
api_secret = 'your_api_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

tweet = "This is a test tweet sent from my Linux terminal using Python. #Linux #Automation"

try:
    api.update_status(tweet)
    print("✅ Tweet sent successfully!")
except Exception as e:
    print("❌ Error sending tweet:", e)
