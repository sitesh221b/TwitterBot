from auth import api
import tweepy
import sys
import time
# import os

# def clear():
#     if os.name == 'nt':             # For Windows
#         _ = os.system("cls")
#     else:                           # For Linux, Mac
#         _ = os.system("clear")


#   The main menu listing all the functionality
def main_menu():
    # clear()
    print("\n\n\t\t\tTWITTER BOT v1.0")
    print("=========================================")
    print("\t\t1. Search a Profile")
    print("\t\t2. Retrieve your tweets")
    print("\t\t3. Send a Message")
    print("\t\t4. Follow someone")
    print("\t\t5. Block a User")
    print("\t\t6. Unblock a User")
    print("\t\t7. Search a hashtag")
    print("\t\t8. Exit")
    c = int(input("Enter your choice: "))
    if c == 1:
        search_profile()
    elif c == 2:
        ret_tweets()
    elif c == 3:
        send_msg()
    elif c == 4:
        follow()
    elif c == 5:
        block()
    elif c == 6:
        unblock()
    elif c == 7:
        search_tweet()
    elif c == 8:
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
    # max_tweets = int(input("Number of tweets you want to retrieve: "))
    # for tweets in tweepy.Cursor(api.user_timeline).items(max_tweets):
    #     print(tweets)
    tweets = api.user_timeline(api.me()._json['screen_name'])
    for i in range(len(tweets)):
        print(i+1, ':', tweets[i]._json['text'])
    input("\nPress Enter to continue...")
    main_menu()


def send_msg():
    user_id = input("Twitter handle to whom you want to send message: ")
    msg = input("Enter your message: ")

    try:
        api.send_direct_message(user_id, text=msg)
    except tweepy.TweepError:
        print("Error: Failed to send message. Try Again Later.")

    input("\nPress Enter to continue...")
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
    input("\nPress Enter to continue...")
    main_menu()


def block():
    user_id = input("Username of whom you want to block: ")
    try:
        api.create_block(user_id)
    except tweepy.TweepError:
        print("Error: Unable to block!")
    else:
        print(user_id + ' is blocked!')
    time.sleep(1)
    input("\nPress Enter to continue...")
    main_menu()


def unblock():
    user_id = input("Username of whom you want to Unblock: ")
    try:
        api.destroy_block(user_id)
    except tweepy.TweepError:
        print("Error: Unable to Unblock!")
    else:
        print(user_id + ' is Unblocked!')
    time.sleep(1)
    input("\nPress any key to continue...")
    main_menu()


def search_tweet():
    query = input("Your Query: ")
    max_search = int(input("Maximum Results: "))
    searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_search)]

    for i in range(len(searched_tweets)):
        print(i+1, ':', searched_tweets[i]._json['text'])

    time.sleep(1)
    input("\nPress Enter to Continue...")
    main_menu()
