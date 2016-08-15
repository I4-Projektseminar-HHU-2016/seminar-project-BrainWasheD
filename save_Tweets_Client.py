import tweepy
import unicodecsv as csv
import codecs

from twitter_keys import consumer_key, consumer_secret, access_token, access_token_secret

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth, wait_on_rate_limit=True)

# Erstellen einer csv Datei
resultFile = open('result.csv', 'ab')
writer = csv.writer(resultFile, 
                    delimiter=";", 
                    lineterminator="\n",
                    encoding='utf-8')
# Ueberschriften reinschreiben
writer.writerow(['Tweet ID', 'Datum yyyy-mm-dd', 'Text'])

# Zuweisung der Nutzer, die gecrawled werden sollen

def fetch_and_write(*args):
# Nutzer fuer Nutzer durchgehen und die einzelnen tweets rausziehen

    for tweet in tweepy.Cursor(api.search, q=args).items():
        if (not tweet.retweeted) and ('RT @' not in tweet.text):
            tweet.text = tweet.text.replace('|', ' ')
            tweet.text = tweet.text.replace('\n', ' ')
            writer.writerow([tweet.id_str, tweet.created_at, tweet.text])
    resultFile.close()

if __name__ == "__main__":
    fetch_and_write('#Warcraft', '#Legion')


########################################################################
#																	   #
#   Der Quellcode beider Dateien wurde in Zusammenarbeit mit Thorsten  #
#   Brueckner geschrieben 											   #
#																	   #
########################################################################
