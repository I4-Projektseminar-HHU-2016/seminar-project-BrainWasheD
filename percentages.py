import re

class percs(object):
    def __init__(self):
        return

    def percent(self, tweets):
        #Counting Tweets that contain a @Mention
        self.count = 0
        self.regex = re.compile('(?<=^|(?<=[^a-zA-Z0-9-\.]))@([A-Za-z0-9_]+)')
        for elem in tweets:
            self.temp = ' '.join(tweets[elem])
            if re.match(self.regex, self.temp) is not None:
                self.count += 1

        self.perc_mentions = round(((100/len(tweets))*self.count), 2)
        print ('tweets: ', len(tweets))
        print ('mentions: ', self.count, self.perc_mentions, '%')
        return
