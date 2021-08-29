import pickle
import tweepy
from tqdm import tqdm
from session import kuma
from meta import write_meta
from init import new_empty_data
from fetch_info import get_info
from fetch_tweets import get_tweets
from datetime import datetime, timedelta


if __name__ == '__main__':
    print('Initializing...')
    now = datetime.now()
    info_date = now.replace(hour=0, minute=0, second=0, microsecond=0)
    info_date_str = info_date.strftime('%Y%m%d')
    print('  info date:', info_date_str)
    tweets_date = now - timedelta(days=2)
    tweets_start = tweets_date.replace(hour=0, minute=0, second=0, microsecond=0)
    tweets_end = tweets_start + timedelta(days=1)
    tweets_date_str = tweets_date.strftime('%Y%m%d')
    print('  tweets date:', tweets_date_str)
    meta_path, info_path, tweets_path = new_empty_data(info_date_str, tweets_date_str)

    print('Getting friends ids...')
    kuma._me = kuma.me()
    friends_ids = kuma.friends_ids()
    friends_ids.append(kuma._me.id)

    print('Getting friends info...')
    with open(info_path, 'rb') as f:
        info_data = pickle.load(f)
    friends_info = info_data.copy()
    for user in tqdm(friends_ids):
        if user not in friends_info:
            try:
                friends_info[user] = get_info(user)
            except tweepy.error.TweepError:
                pass
    if not info_data == friends_info:
        with open(info_path, 'wb') as f:
            pickle.dump(friends_info, f)

    print('Getting friends tweets...')
    with open(tweets_path, 'rb') as f:
        tweets_data = pickle.load(f)
    friends_tweets = tweets_data.copy()
    for user in tqdm(friends_ids):
        if user not in friends_tweets:
            try:
                friends_tweets[user] = get_tweets(user, tweets_start, tweets_end)
            except tweepy.error.TweepError:
                pass
    if not tweets_data == friends_tweets:
        with open(tweets_path, 'wb') as f:
            pickle.dump(friends_tweets, f)

    print('Writing meta info...')
    write_meta(meta_path, friends_ids, now, tweets_date)

    print('Done.')
