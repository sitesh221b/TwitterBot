import tweepy
import os

api = 0


def clear():
    if os.name == 'nt':             # For Windows
        _ = os.system("cls")
    else:                           # For Linux, Mac
        _ = os.system("clear")


def authentication():
    global api
    print("For security reasons you'll have to enter Consumer Key & Access Token here only:\n")

    #   Taking tokens & keys from the user
    consumer_key = input("Consumer Key: ")
    consumer_secret = input("Consumer Secret: ")
    access_token = input("Access Token: ")
    access_key = input("Access Key: ")

    #   Authorizing those tokens & keys
    oauth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    oauth.set_access_token(access_token, access_key)

    try:
        api = tweepy.API(oauth)
    except tweepy.TweepError:
        print("The Program faced an Error while authorizing the user!\nPlease run the program again.")
7