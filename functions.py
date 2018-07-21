#from main import *
import tweepy
import time
import sys
import os

global api

# def clear():
#     if os.name == 'nt':             # For Windows
#         _ = os.system("cls")
#     else:                           # For Linux, Mac
#         _ = os.system("clear")


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

if api:
    print("\nValidation Successful!")
    time.sleep(1)
    print("Starting the Bot....")
    time.sleep(2)


#   The main menu with all the functionality
def main_menu():
    # clear()
    print("\n\n\t\t\tTWITTER BOT v1.0")
    print("=========================================")
    print("\t\t1. Search a Profile")
    print("\t\t2. Retrieve your tweets")
    print("\t\t3. Send a Message")
    print("\t\t4. Follow someone")
    print("\t\t5. Block/Unblock")
    print("\t\t6. Search a hashtag")
    print("\t\t7. Exit")

    c = int(input("Enter your choice: "))
    if c == 1:
        search_profile()
    elif c == 2:
        ret_tweets()
    elif c == 3:
        send_msg()
    elif c == 4:
        follow()
    # elif c == 5:
    #   block_unblock()
    # elif c == 6:
    #   search_tweet()
    elif c == 7:
        sys.exit(0)
    else:
        print("Invalid Option!")
        time.sleep(2)
        main_menu()


def search_profile():
    user_id = input("Enter the username/ID: ")
    data = api.get_user(user_id)._json
    print("Name: "+data['name'])
    print("Location: "+data['location'])
    print("Followers: ", data['followers_count'])
    print("Following: ", data['friends_count'])
    input("\nPress Enter to continue...")
    main_menu()


def ret_tweets():
    tweets = api.user_timeline()
    # print(api.user_timeline()[0]._json['text'])           <------ DOUBT
    tmp = []
    tweets_in_file = [tweet.text for tweet in tweets]   # CSV File created
    for i in tweets_in_file:
        tmp.append(i)
    for i in range(20):
        print(i+1, ": ", tmp[i])
    input("\nPress Enter to continue...")
    main_menu()


def send_msg():
    user_id = input("Twitter handle to whom you want to send message: ")
    msg = input("Enter your message: ")

    try:
        api.send_direct_message(user_id, text=msg)
    except tweepy.TweepError:
        print("Error: Failed to send message. Try Again Later.")

    input("Press Enter to continue...")
    main_menu()


def follow():
    user_id = input("Twitter ID of whom you want to follow: ")

    try:
        api.create_friendship(user_id)
    except tweepy.TweepError:
        print("Error: Please try again later")
    else:
        print("Follow request sent...")
    time.sleep(1)
    input("Press Enter to continue...")
    main_menu()


# def block_unblock():


# def search_tweet():


main_menu()
