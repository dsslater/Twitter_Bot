import tweepy
import top_stories
import nl_substitutions
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

queries1 = ['', 'news', 'politics', 'congress', 'election', 'trump', 'iowa', 'bush', 'clinton', 'rubio', 'media', 'poll']
queries2 = ['movie', 'music', 'science', 'sports', 'space', 'award', 'movement', 'entertainment', 'hollywood', 'markets', 'animals', 'economy']

if __name__ == "__main__":
    twitter = TwitterAPI()
    tweet = False
    while tweet == False:
        politics_story = top_stories.get_story(queries1[random.randint(0, len(queries1)-1)])
        soft_story = top_stories.get_story(queries2[random.randint(0, len(queries2)-1)])
        if politics_story != None and soft_story != None:
            tweet = nltk_test.new_headline(soft_story[0], politics_story[0])
    twitter.tweet(tweet)
