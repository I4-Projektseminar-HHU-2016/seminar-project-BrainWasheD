import re
import matplotlib.pyplot as plt
import numpy as np
from os import path
from matplotlib import cm


class percs(object):
    def __init__(self):
        return

    def percent(self, tweets, mentions, mtcount):

        print ('creating mention graphs...')
        #Counting Tweets that contain a @Mention
        self.count = 0
        self.regex = re.compile('(?<=^|(?<=[^a-zA-Z0-9-\.]))@([A-Za-z0-9_]+)')
        
        for elem in tweets:
            self.temp = ' '.join(tweets[elem])
            if re.match(self.regex, self.temp) is not None:
                self.count += 1

        self.perc_mentions = round(((100/len(tweets))*self.count), 2)

        self.labels = []
        self.sizes = []
        self.mt = 0

        for elem in mentions:
            (self.key, self.value) = elem
            self.labels.append(self.key+': '+str(self.value))
            self.sizes.append(self.value)
            self.mt += self.value

        self.labels.append('Counted Mentions: '+str(mtcount))
        self.sizes.append(mtcount-self.mt)

        self.colors = cm.Set1(np.arange(26)/26.)
        self.fig = plt.figure(1)
        self.ax = self.fig.add_subplot(111)

        self.patches, self.texts = self.ax.pie(self.sizes, colors=self.colors, shadow=True, startangle=90)

        self.lgd = self.ax.legend(self.patches, self.labels, loc='center right', bbox_to_anchor=(1.5, 0.5))
        self.ax.axis('equal')
        self.fig.savefig(path.join(path.dirname(__file__), 'RESULTS/mentions.png'), transparent=True, bbox_extra_artists=(self.lgd,), bbox_inches='tight')
        plt.close()

        self.twc = (len(tweets)-self.count)
        
        self.patches2, self.texts2 = plt.pie([self.twc, self.count], colors=['red', 'blue'], shadow=True, startangle=90)
        plt.legend(self.patches2, ['Tweets: '+str(len(tweets)), 'Mentions: '+str(self.count)], loc='best')
        plt.axis('equal')
        plt.tight_layout()
        plt.savefig(path.join(path.dirname(__file__), 'RESULTS/mentions_percentage.png'), transparent=True)
        plt.close()
        
        return
