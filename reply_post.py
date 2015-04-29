import praw
import pdb
import re
import os
from config_bot import *
if not os.path.isfile("config_bot.py"):
    print("You must create a config_bot.py file with the pass and usernames.")
    print("PLEASE DO SO")
    exit(1)
user_agent = ("YourFriend 0.1")
r = praw.Reddit(user_agent = user_agent)
r.login(REDDIT_USERNAME, REDDIT_PASS)
if not os.path.isfile("post_replies.txt"):
    post_replies = []
else:
    with open("post_replies.txt","a") as f:
        post_replies = f.read()
        post_replies = post_replies.split("\n")
        post_replies = filter(None, post_replies)
subreddit = r.get_subreddit('bottingbottingbotted')
for submission in subreddit.get_new(limit=5):
    if submission.id not in post_replies:
        if re.search("i need a friend", submission.title, re.IGNORECASE):
            submission.add_comment("I will be your friend!")
            print("Bot Replying to: ", submission.title)
            post_replies.append(submission.id)
            with open("post_replies.txt", "w") as f:
                for post_id in post_replies:
                    f.write(post_id + "\n")
