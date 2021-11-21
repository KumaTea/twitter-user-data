import tweepy
from session import kuma
from datetime import datetime, timedelta


def slim_status(status):
    delattr(status, 'user')
    delattr(status, '_json')
    return status


def get_tweets(user_id, date, end_date=None, slim=True):
    if not end_date:
        end_date = date + timedelta(days=1)
    # user_info = kuma.get_user(user_id)

    user_tweets = []
    for status in tweepy.Cursor(
            kuma.user_timeline, user_id=user_id,
            trim_user=True, exclude_replies=False, include_rts=False,
            count=200).items():
        if status.created_at >= end_date:
            pass
        elif date <= status.created_at < end_date:
            if slim:
                status = slim_status(status)
            user_tweets.append(status)
        else:  # status.created_at < date
            break
    # print('Total:', len(user_tweets))
    return user_tweets
