from auth import *

# api.get_user("TwitterID")                         ->      Search a User
# api.me()                                          ->      My Profile
# api.user_timeline("TwitterID")                    ->      Top 20 tweets
# api.search_users()                                ->      Find People
# api.send_direct_message("TwitterID", text="")     ->      Send message to your follower
# api.friends_ids("TwitterID")                      ->      Array of ID's of users being followed by the specified user
# api.followers_ids("TwitterID")                    ->      Array of ID's of users following the specified user

# print(api.get_user("iamsrk"))

#   The main menu with all the functionality


# def main_menu():
#     clear()
#     print("\t\t\tTWITTER BOT v1.0")
#     print("\t\t1. Your Profile")
#     print("\t\t2. Retrieve your tweets")
#     print("\t\t3. Send a Message")
#     print("\t\t4. Follow someone")
#     print("\t\t5. Block/Unblock")
#     print("\t\t6. Search a hashtag")


if __name__ == '__main__':
    authentication()
    # main_menu()
