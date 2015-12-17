import tweepy
import top_stories
import nl_substitutions
import random

queries1 = ['', 'news', 'politics', 'congress', 'election', 'trump', 'iowa', 'bush', 'clinton', 'rubio', 'media', 'poll']
queries2 = ['movie', 'music', 'science', 'sports', 'space', 'award', 'movement', 'entertainment', 'hollywood', 'markets', 'animals', 'economy']

#tweepy implementation
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

"""
Randomly chooses a political and then a soft news story. 
These two stories are then passed to new_headline where 
there is an attempt to 'mash' them. If this is successful 
the new headline in tweeted. Otherwise a new combination 
is tried.
"""
if __name__ == "__main__":

    twitter = TwitterAPI()
    tweet = False
    while tweet == False:
        politics_story = top_stories.get_story(queries1[random.randint(0, len(queries1)-1)])
        soft_story = top_stories.get_story(queries2[random.randint(0, len(queries2)-1)])
        print(politics_story, soft_story)
        if politics_story != None and soft_story != None:
            print(tweet)
            tweet = nltk_test.new_headline(soft_story, politics_story)
    twitter.tweet(tweet)
