import praw
import time

reddit = praw.Reddit(
    ##ENTER YOUR REDDIT API INFORMATION HERE
    client_id="",
    client_secret="",
    password="",
    user_agent="",
    username="",
)


subreddits = ['Referral', 'referralcodes', 'Referrals', 'promocodes',]

link = ##Enter your referral link
title = ##Enter the title of your post

for subreddit in subreddits:
    try:
        reddit.subreddit(subreddit).submit(title, url=link, send_replies=False)
        print("successfully posted to ", subreddit)
    except praw.exceptions.APIException as exception:
        if exception.error_type == "RATELIMIT":
            wait = str(exception).replace("RATELIMIT: 'you are doing that too much, try again in ", "")
            if 'minute' in wait:
                wait = wait[:2]
                wait = int(wait)
                print(wait)
            else:
                wait = 1
            time.sleep(wait*60)
            reddit.subreddit(subreddit).submit(title, url=link, send_replies=False)
            print("successfully posted to ", subreddit)
    except Exception as e:
        print(f"Error: {e}")
