from credentials import consumer_key, consumer_secret
from credentials import acess_token, acess_token_secret
import tweepy
import time

# Authenticate the access to twitter api,
# with credentials obtained from developer twitter.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acess_token, acess_token_secret)

# Connects to the twitter api through the authentication data
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()


def tweets_fav_and_rt(search_sentence, num_limit):
    """ Fav and RT tweets

    Arguments:
        search_sentence {str} -- search for predefined sentences on twitter
        num_limit {int} -- number of fav's and rt's in one loop (limit)
    """
    for tweet in tweepy.Cursor(api.search, search_sentence).items(num_limit):
        try:
            tweet.favorite()
            tweet.retweet()
            print(f"tweet favorited and retweeted: {tweet.text}")
            time.sleep(10)
        except tweepy.TweepError as error:
            print(f"error! reason: {error.reason}")
        except StopIteration:
            print("finish!")
            break


search_sentence = "any sentence you wanna search"
num_limit = 10
tweets_fav_and_rt(search_sentence, num_limit)
