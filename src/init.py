import os
import pickle
from tools import mkdir


def new_empty_data(info_date: str, tweets_date: str):
    mkdir('../data')
    mkdir('../data/info')
    mkdir('../data/tweets')

    meta_path = '../data/meta.p'
    info_path = f'../data/info/{info_date}.p'
    tweets_path = f'../data/tweets/{tweets_date}.p'

    for i in [meta_path, info_path, tweets_path]:
        if not os.path.isfile(i):
            with open(i, 'wb') as f:
                pickle.dump({}, f)

    return meta_path, info_path, tweets_path
