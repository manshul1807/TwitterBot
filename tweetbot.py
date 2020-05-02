import tweepy
import time

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

Get the User object for twitter...
user = api.get_user('kunalkamra88')
print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
    print(friend.screen_name)

user = api.me()
print(user.name)
print(user.screen_name)
print(user.followers_count)


def limit_handle(cursor):
    while True:
        try:
            yield cursor.next()
        except StopIteration:
            return
        except tweepy.RateLimitError:
            time.sleep(1*60)


# generous bot

for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    if follower.name == 'Andrew Vcourt':
        follower.follow()


# favorite bot
search_string = 'Manshul'
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try:
        tweet.favorite()
        print('I liked the tweet!!')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
