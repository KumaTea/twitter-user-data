import pickle


old_date = '20210122'
last_date = '20210821'
min_tweets = 100


def slim_tweets(data):
    new_data = data.copy()
    del_count = 0
    for user in data:
        if len(data[user]['tweets']) < min_tweets:
            new_data.pop(user, '')
    del_count += 1
    print('Del:', del_count)
    return new_data


print('Loading', old_date)
with open(f'../data/{old_date}_fmt.p', 'rb') as f:
    old_friends_tweets = pickle.load(f)
slim_old_friends_tweets = slim_tweets(old_friends_tweets)
print('Writing', old_date)
with open(f'../data/{old_date}_slim.p', 'wb') as f:
    pickle.dump(slim_old_friends_tweets, f)


print('Loading', last_date)
with open(f'../data/{last_date}_raw.p', 'rb') as f:
    friends_tweets = pickle.load(f)
slim_friends_tweets = slim_tweets(friends_tweets)
print('Writing', last_date)
with open(f'../data/{last_date}_slim.p', 'wb') as f:
    pickle.dump(slim_friends_tweets, f)
