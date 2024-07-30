# tweet_post.py
import tweepy

# Twitter API credentials (Replace with your own keys and tokens)
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Create a tweet
tweet = "
🌟 Excited to announce our new project: [PDF to Text Converter App](https://github.com/hmltn-0/pdf-to-text-app) 🚀

This versatile app converts PDFs to text, with future plans for various editing functions.

---** Features **---
- Convert PDFs to plain text, Markdown, and LaTeX
- User-friendly GUI with PyQt5
- Merge and split PDFs, annotate, redact, fill forms, cloud integration in the future

We are open to funding opportunities to bring this vision to life! 💡

#PDF #Tech #Startup #Investment #SoftwareDevelopment
"

# Post tweet
api.update_status(tweet)

'''
This script uses the Tweepy library to post a tweet.

To use:
1. Replace the placeholders with your Twitter API credentials.
2. Run the script to post the tweet.
'''

