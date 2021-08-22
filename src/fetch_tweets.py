import sys
import pickle
import tweepy
from tqdm import tqdm
from session import kuma
from datetime import datetime


now = datetime.now()
a_day_ago = datetime(now.year, now.month, now.day-1, 0, 0, 0, 0)
half_year = datetime(now.year, now.month-6, now.day, 0, 0, 0, 0)
date_string = a_day_ago.strftime('%Y%m%d')

kuma._me = kuma.me()
print('Getting friends_ids...')
friends_ids = kuma.friends_ids()

# old_friends_latest_tweets = {}
# with open('../data/old_friends_latest_tweets.json', 'r') as f:
#     tmp = json.load(f)
# for i in tmp:
#     old_friends_latest_tweets[int(i)] = tmp[i]
# del tmp


def get_tweets(user_id):
    user_info = kuma.get_user(user_id)
    user_tweets = []
    print('Getting:', user_info.screen_name)

    for status in tweepy.Cursor(
            kuma.user_timeline, user_id,
            trim_user=True, exclude_replies=True, include_rts=False,
            count=200).items():
        if status.created_at < a_day_ago:
            sys.stdout.write('\r' + f'Get: {status.id}, {status.created_at}')
            user_tweets.append(status)
        else:
            sys.stdout.write('\r' + f'Skip: {status.id}, {status.created_at}')

    print('Total:', len(user_tweets))
    return user_info, user_tweets


try:
    with open(f'../data/{date_string}_raw.p', 'rb') as f:
        friends_tweets = pickle.load(f)
except FileNotFoundError:
    friends_tweets = {}
friends_ids.append(kuma._me.id)


print('Getting friends_tweets')
for user in tqdm(friends_ids):
    if user in friends_tweets:
        print('Skip:', user)
    else:
        user_res = get_tweets(user)
        friends_tweets[user] = {
            'info': user_res[0],
            'tweets': user_res[1]
        }


print('Writing friends_tweets')
with open(f'../data/{date_string}_raw.p', 'wb') as f:
    pickle.dump(friends_tweets, f)
