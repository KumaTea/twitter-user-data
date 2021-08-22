import pickle


old_date = '20210122'
last_date = '20210821'

print('Loading', old_date)
with open(f'../data/{old_date}_raw.p', 'rb') as f:
    old_friends_tweets = pickle.load(f)

print('Loading', last_date)
with open(f'../data/{last_date}_raw.p', 'rb') as f:
    new_friends_tweets = pickle.load(f)


formatted_old_friends_tweets = {}

for friend in old_friends_tweets:
    if friend in new_friends_tweets:
        formatted_old_friends_tweets[friend] = {
            'info': new_friends_tweets[friend]['info'],
            'tweets': old_friends_tweets[friend]
        }

print('Writing', old_date)
with open(f'../data/{old_date}_fmt.p', 'wb') as f:
    pickle.dump(formatted_old_friends_tweets, f)
