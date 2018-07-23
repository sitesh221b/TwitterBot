import tweepy

# print("For security reasons you'll have to enter Consumer Key & Access Token here only:\n")

# Taking tokens & keys from the user
# consumer_key = input("Consumer Key: ")
# consumer_secret = input("Consumer Secret: ")
# access_token = input("Access Token: ")
# access_key = input("Access Key: ")

consumer_key = "6hzEVn8PgapYRdE3m5cxNFuPt"
consumer_secret = "oOw3lpNSoqQnevZ9yn9Y5u5UCs2naXRTsoPRyFfsZpRh5kq4cs"
access_token = "842271726855585792-PiJRsYaKqCn4oy32Y4WHXT9iFWCxSyQ"
access_key = "XiuK3xGKtcZB8IqZMv2OTGn0vjGZ9qbkwBJAwShBJzHlL"

#   Authorizing those tokens & keys
oauth = tweepy.OAuthHandler(consumer_key, consumer_secret)
oauth.set_access_token(access_token, access_key)

try:
    api = tweepy.API(oauth)
except tweepy.TweepError:
    print("The Program faced an Error while authorizing the user!\nPlease run the program again.")
    exit(0)
