import csv
import time
import pickle
from tqdm import tqdm
from datetime import datetime
from get_factors import get_user_factors

old_date = '20210122'
last_date = '20210821'
fetch_date = datetime(2021, 8, 22, 0, 0, 0)

header = ['tid', 'yr', 'mo', 'dt', 'wk', 'dow', 'doy', 'time', 'last', 'nxt', 'tlen', 'media', 'src', 'isq', 'sen', 'lang',
          'snlen', 'prot', 'foing', 'foer', 'crd', 'favcnt', 'tcnt',
          'lcnt']


# def process_data(date):
#     print('Reading pickle...', end='')
#     t0 = time.time()
#     with open(f'../data/{date}_slim.p', 'rb') as f:
#         data = pickle.load(f)
#     print(int(time.time() - t0))
#
#     print('Generating data...', end='')
#     t0 = time.time()
#     result = []
#     for user in tqdm(data):
#         user_result = get_user_factors(data[user], now=fetch_date)
#         result.extend(user_result)
#     print(int(time.time() - t0))
#     return result
#
#
# def write_csv(date):
#     with open(f'../data/{date}.csv', 'w', encoding='utf-8', newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow(header)
#         data = process_data(date)
#         t0 = time.time()
#         print('Writing csv...', end='')
#         writer.writerows(data)
#         print(int(time.time() - t0))


def write_csv(date):
    with open(f'../data/{date}.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        print('Reading pickle...', end='')
        t0 = time.time()
        with open(f'../data/{date}_slim.p', 'rb') as f:
            data = pickle.load(f)
        print(int(time.time() - t0))

        print('Generating data...', end='')
        t0 = time.time()
        for user in tqdm(data):
            user_result = get_user_factors(data[user], now=fetch_date)
            writer.writerows(user_result)
        print(int(time.time() - t0))


if __name__ == '__main__':
    write_csv(old_date)
    write_csv(last_date)
