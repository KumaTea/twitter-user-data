from tools import *
# from tqdm import tqdm
from fastai.tabular.all import *
from bs4 import BeautifulSoup as bs


def get_tid(tweet):
    return tweet.id


def get_dates(tweet):
    date = to_cst(tweet.created_at)
    df = pd.DataFrame({'date': [date]})
    make_date(df, 'date')
    df = add_datepart(df, 'date')
    # Year	Month	Week	Day	Dayofweek	Dayofyear
    df_iloc = df.iloc[:, :6]
    yr, mo, wk, dt, dow, doy = df_iloc.values[0]
    return yr, mo, dt, wk, dow, doy


def get_time(tweet):
    date = to_cst(tweet.created_at)
    since_midnight = date - date.replace(hour=0, minute=0, second=0, microsecond=0)
    return since_midnight.seconds


def get_created_date(user):
    return to_cst(user.created_at)


def get_created_days(user, now=None):
    if not now:
        now = datetime.now()
    return (now - get_created_date(user)).days


def get_tweet_freq(user, then=None, tweet=None, exp=True, now=None):
    assert then or tweet
    if not then:
        then = tweet.created_at
    crd = get_created_days(user, now)
    total_tweets = user.statuses_count
    if exp:
        crd_then = get_created_days(user, to_cst(then))
        total_tweets_then = exp_calc(crd, total_tweets, crd_then)
        try:
            tweet_freq = total_tweets_then / crd_then
        except ZeroDivisionError:
            return 0
    else:
        tweet_freq = total_tweets / crd

    return tweet_freq


def get_intervals(user, all_tweets, tweet=None, tweet_index=None):
    assert tweet or tweet_index
    if not tweet:
        tweet = all_tweets[tweet_index]
    elif not tweet_index:
        tweet_index = all_tweets.index(tweet)

    if tweet_index == 0:  # first
        tfrq = get_tweet_freq(user, tweet.created_at, tweet)
        next_sec = tfrq
        last_sec = (tweet.created_at - all_tweets[tweet_index + 1].created_at).seconds
    elif tweet_index == len(all_tweets) - 1:  # last
        tfrq = get_tweet_freq(user, tweet.created_at, tweet)
        next_sec = (tweet.created_at - all_tweets[tweet_index - 1].created_at).seconds
        last_sec = tfrq
    else:
        next_sec = (tweet.created_at - all_tweets[tweet_index - 1].created_at).seconds
        # until next newer tweet
        last_sec = (tweet.created_at - all_tweets[tweet_index + 1].created_at).seconds

    return next_sec, last_sec


def get_tweet_length(tweet):
    return len(tweet.text)


def get_media(tweet):
    if 'media' in tweet.entities:
        if tweet.extended_entities['media'][0]['type'] == 'photo':
            return 'pic' + str(len(tweet.extended_entities['media']))
        elif tweet.extended_entities['media'][0]['type'] == 'animated_gif':
            return 'gif'
        elif tweet.extended_entities['media'][0]['type'] == 'video':
            return 'video'
    else:
        return 'text'


def get_source(tweet):
    if '<a' in tweet.source:
        soup = bs(tweet.source)
        return soup.find('a').text
    else:
        return tweet.source


def get_is_quoted_status(tweet):
    return tweet.is_quote_status


def get_sensitivity(tweet):
    if hasattr(tweet, 'possibly_sensitive'):
        return tweet.possibly_sensitive
    else:
        return False


def get_language(tweet):
    return tweet.lang


def get_username_length(user):
    return len(user.screen_name)


def get_is_protected(user):
    return user.protected


def get_user_info(user, then=None, tweet=None, exp=True, now=None):
    assert then or tweet
    if not then:
        then = tweet.created_at
    crd = get_created_days(user, now)
    foing = user.friends_count
    foer = user.followers_count
    favcnt = user.favourites_count
    tcnt = user.statuses_count
    if exp:
        crd_then = get_created_days(user, to_cst(then))
        foing_then = exp_calc(crd, foing, crd_then)
        foer_then = exp_calc(crd, foer, crd_then)
        favcnt_then = exp_calc(crd, favcnt, crd_then)
        tcnt_then = exp_calc(crd, tcnt, crd_then)
        return foing_then, foer_then, favcnt_then, tcnt_then
    else:
        return foing, foer, favcnt, tcnt


def get_likes(tweet):
    return tweet.favorite_count


def get_user_factors(user_data, now=None):
    user_info = user_data['info']
    user_tweets = user_data['tweets']

    tabular_data = []
    # for tweet_index in tqdm(range(len(user_tweets))):
    for tweet_index in range(len(user_tweets)):
        tweet = user_tweets[tweet_index]

        tid = get_tid(tweet)
        yr, mo, dt, wk, dow, doy = get_dates(tweet)
        time = get_time(tweet)
        nxt, last = get_intervals(user_info, user_tweets, tweet, tweet_index)
        tlen = get_tweet_length(tweet)
        media = get_media(tweet)
        src = get_source(tweet)
        isq = get_is_quoted_status(tweet)
        sen = get_sensitivity(tweet)
        lang = get_language(tweet)

        snlen = get_username_length(user_info)
        prot = get_is_protected(user_info)
        foing, foer, favcnt, tcnt = get_user_info(user_info, to_cst(tweet.created_at), now=now)
        crd = get_created_days(user_info, to_cst(tweet.created_at))

        lcnt = get_likes(tweet)

        tabular_data.append(
            [tid, yr, mo, dt, wk, dow, doy, time, last, nxt, tlen, media, src, isq, sen, lang,
             snlen, prot, foing, foer, crd, favcnt, tcnt,
             lcnt]
        )

    return tabular_data
