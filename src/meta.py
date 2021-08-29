import pickle


def write_meta(meta_path, users: list, info_date, tweets_date):
    with open(meta_path, 'rb') as f:
        meta = pickle.load(f)
    for user in users:
        meta[user] = {
            'info': info_date,
            'tweets': tweets_date
        }
    with open(meta_path, 'wb') as f:
        pickle.dump(meta, f)
