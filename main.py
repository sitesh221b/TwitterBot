from functions import *
from auth import *

# api.get_user("TwitterID")                         ->      Search a User
# api.me()                                          ->      My Profile
# api.user_timeline("TwitterID")                    ->      Top 20 tweets
# api.search_users()                                ->      Find People
# api.send_direct_message("TwitterID", text="")     ->      Send message to your follower
# api.friends_ids("TwitterID")                      ->      Array of ID's of users being followed by the specified user
# api.followers_ids("TwitterID")                    ->      Array of ID's of users following the specified user
# api.create_friendship("TwitterID")                ->      Send follow request
# api.create_block("TwitterID")                     ->      Block someone
# api.destroy_block("TwitterID")                    ->      Unblock someone
# api.search("query")                               ->      list of search results objects


# if __name__ == '__main__':
#     api = authentication()
#     print(api)
#     main_menu()
