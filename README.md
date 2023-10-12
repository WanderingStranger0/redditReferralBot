# redditReferralBot

Overview
The Reddit Referral Bot is a Python script designed to automate the process of posting referral links to Reddit. It handles rate limiting and operates efficiently with minimal dependencies. The bot utilizes the PRAW library for interacting with the Reddit API and the time module for managing time intervals.

Prerequisites

Python 3.x installed on your system.

Reddit API credentials (client ID, client secret, user agent) obtained from the Reddit developer portal.


Installation

Clone the repository to your local machine:

git clone https://github.com/WanderingStranger0/redditReferralBot.git



Navigate to the project directory:

cd redditReferralBot


Install the required dependencies using pip:

pip install -r requirements.txt



Configuration

Open redditReferralBot.py in a text editor.

Add your Reddit API credentials:


# Reddit API credentials

CLIENT_ID = 'your_client_id'

CLIENT_SECRET = 'your_client_secret'

USER_AGENT = 'your_user_agent'

Customize the message that will be posted:



Usage
Run the bot script:

python redditReferralBot.py

The bot will start posting the specified message with your referral link to the specified subreddit(s) at the defined intervals.


Important Note

Please use this bot responsibly and adhere to Reddit's terms of service and community guidelines. Avoid spamming, respect the rules of the subreddits you are posting in, and ensure that your posts provide value to the community.

License

This project is licensed under the MIT License - see the LICENSE file for details.


Happy Botting! 🤖✨

