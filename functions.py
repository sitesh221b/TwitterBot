from auth import api
import tweepy
import paralleldots as pd
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
    print("\t\t3. Tweet a Message")
    print("\t\t4. Send a Message")
    print("\t\t5. See Trending Tweets")
    print("\t\t6. Follow someone")
    print("\t\t7. Block a User")
    print("\t\t8. Unblock a User")
    print("\t\t9. Search a Hash-tag")
    print("\t\t10. Exit")
    c = int(input("Enter your choice: "))
    if c == 1:
        search_profile()
    elif c == 2:
        ret_tweets()
    elif c == 3:
        tweet_status()
    elif c == 4:
        send_msg()
    elif c == 5:
        trend_tweets()
    elif c == 6:
        follow()
    elif c == 7:
        block()
    elif c == 8:
        unblock()
    elif c == 9:
        search_tweet()
    elif c == 10:
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
    print("Language: "+data['lang'])
    print("Followers: ", data['followers_count'])
    print("Following: ", data['friends_count'])
    print("Created At: "+data['created_at'])
    print("Description: ", data['description'])
    print("URL: "+data['url'])
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


def tweet_status():
    text = input('Write your tweet: ')
    try:
        api.update_status(text)
    except tweepy.TweepError:
        print("Error: Unable to tweet! Try Again.")
    else:
        print("Tweeted!")
    time.sleep(1)
    input("\nPress Enter to continue...")
    main_menu()


def send_msg():
    user_id = input("Twitter handle to whom you want to send message: ")
    msg = input("Enter your message: ")

    try:
        api.send_direct_message(user_id, text=msg)
    except tweepy.TweepError:
        print("Error: Failed to send message. Try Again Later.")
    else:
        print("Message Sent.")
    time.sleep(1)
    input("\nPress Enter to continue...")
    main_menu()


def trend_tweets():
    n = int(input("Number of top trends you want see(max 50): "))
    while n < 0 or n > 50:
        print("Incorrect input.")
        time.sleep(1)
        n = int(input("Number of top trends you want see(max 50): "))

    try:
        trends = api.trends_place(1)[0]['trends']
    except tweepy.TweepError:
        print("Error: Please Try Again!")
        time.sleep(1)
        main_menu()
    else:
        trends = {trend['name']: trend['tweet_volume'] for trend in trends}
        trends = {k: trends[k] for k in list(trends.keys())[:n]}
        print("\nHere are top %d tweets with number of tweets:" % n)
        for key in trends:
            print(key+':', trends[key], '\n')
        time.sleep(1)
        input("\nPress Enter to continue...")
        main_menu()


def follow():
    user_id = input("Twitter ID of whom you want to follow: ")
    try:
        api.create_friendship(user_id)
    except tweepy.TweepError:
        print("Error: The Username doesn't exist")
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
    print('\n')
    searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_search)]

    for i in range(len(searched_tweets)):
        json = searched_tweets[i]._json
        json_user = json['user']
        user = json_user['name']
        twitter_id = json_user['screen_name']
        created_at = json['created_at']
        tweet = json['text']
        loc = json_user['location']
        lang = json_user['lang']
        t_zone = json_user['time_zone']
        sentiment = pd.sentiment(tweet)['sentiment']
        emotion = max(pd.emotion(tweet)['emotion']['probabilities'])
        abuse = pd.abuse(tweet)['sentence_type']
        print(str(i+1)+'.\tUser: '+user+' (@'+twitter_id+')')
        print('\tTweet Created: '+created_at)
        print('\tLocation: '+loc)
        print('\tLanguage: '+lang)
        print('\tTime Zone: ', t_zone)
        print('\tTweet: '+tweet)
        print('\n\tSentiment Analysis:\n')
        print('\t\tSentiment: '+sentiment)
        print('\t\tEmotion: '+emotion)
        print('\t\tAbuse: '+abuse)
        print('-------------------------------------------------------------------------------------------------------')
        time.sleep(0.2)

    time.sleep(1)
    input("\nPress Enter to Continue...")
    main_menu()
