import pickle


old_date = '20210122'
last_date = '20210821'
min_tweets = 100


def sort_tweets(data):
    for user in data:
        data[user]['tweets'] = sorted(data[user]['tweets'], key=lambda x: int(x.created_at.timestamp()), reverse=True)
    return data


print('Loading', old_date)
with open(f'../data/{old_date}_slim.p', 'rb') as f:
    old_friends_tweets = pickle.load(f)
sorted_old_friends_tweets = sort_tweets(old_friends_tweets)
if sorted_old_friends_tweets != old_friends_tweets:
    print('Writing', old_date)
    with open(f'../data/{old_date}_slim.p', 'wb') as f:
        pickle.dump(sorted_old_friends_tweets, f)


print('Loading', last_date)
with open(f'../data/{last_date}_slim.p', 'rb') as f:
    friends_tweets = pickle.load(f)
sorted_friends_tweets = sort_tweets(friends_tweets)
if sorted_friends_tweets != friends_tweets:
    print('Writing', last_date)
    with open(f'../data/{last_date}_slim.p', 'wb') as f:
        pickle.dump(sorted_friends_tweets, f)
