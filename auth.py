import tweepy
import paralleldots as pd

pd_key = "RLIqcsE8Vx7A7TcPq2LInhC0i4TR6wxvFRinLtfNMVA"
print("\nFor security reasons you'll have to enter Consumer Key & Access Token here only:\n")

# Taking tokens & keys from the user
consumer_key = input("Consumer Key: ")
consumer_secret = input("Consumer Secret: ")
access_token = input("Access Token: ")
access_key = input("Access Key: ")

#   Authorizing those tokens & keys
oauth = tweepy.OAuthHandler(consumer_key, consumer_secret)
oauth.set_access_token(access_token, access_key)

try:
    api = tweepy.API(oauth)
    pd.set_api_key(pd_key)
except tweepy.TweepError:
    print("The Program faced an Error while authorizing the user!\nPlease run the program again.")
    exit(0)

