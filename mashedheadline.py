import tweepy
import top_stories
import nltk_test
import random

class TwitterAPI:
    def __init__(self):
        consumer_key = ""
        consumer_secret = ""
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = ""
        access_token_secret = ""
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)

queries1 = ['', 'news', 'politics', 'congress', '2016']
queries2 = ['movie', 'science', 'sports', 'space', 'award', 'movement']

if __name__ == "__main__":
    twitter = TwitterAPI()
    sports_story = top_stories.get_story(queries1[random.randint(0, len(queries1))])
    politics_story = top_stories.get_story(queries2[random.randint(0, len(queries2))])
    tweet = nltk_test.new_headline(sports_story[0], politics_story[0])
    twitter.tweet(tweet)
