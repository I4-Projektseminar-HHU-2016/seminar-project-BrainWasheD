 # -*- coding: utf-8 -*-
import tweepy
import unicodecsv as csv
from twitter_keys import consumer_key, consumer_secret, access_token, access_token_secret

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


def start_stream():
        try:
                api = tweepy.streaming.Stream(auth, TwitterStreamListener(), timeout=60, compression=True)
                api.filter(follow = None, track = ['#Warcraft', '#Legion'])
        except IncompleteRead:
                pass
                

class TwitterStreamListener(tweepy.StreamListener):
        
        tweet_count = 0
    
        def on_status(self, tweet):
                if (not tweet.retweeted) and ('RT @' not in tweet.text):
                        tweet.text = tweet.text.replace('|', ' ')
                        tweet.text = tweet.text.replace('\n', ' ')

                        TwitterStreamListener.tweet_count += 1
                        
                        with open('result.csv', 'ab') as resultFile:
                                writer = csv.writer(resultFile,
                                                delimiter=";",
                                                lineterminator="\n",
                                                encoding='utf-8')
                                writer.writerow([tweet.id_str, tweet.created_at, tweet.text])
                        print (TwitterStreamListener.tweet_count)

        def on_timeout(self):
                print ("Timeout... restarting...")
                time.sleep(15)
                start_stream()

        def on_limit(self):
                print ("Limit reached... restarting...")
                time.sleep(15)
                start_stream()


if __name__ == "__main__":
        start_stream()

