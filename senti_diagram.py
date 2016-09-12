import matplotlib.pyplot as plt
from os import path

class sentimentDiagram(object):
    def __init__(self):
        return

    #Takes the results of sentiment.py and creates a pie-diagram of it
    def diagram(self, data):

        self.labels = ['positive: '+str(data[0]), 'negative: '+str(data[1]), 'neutral: '+str(data[2])]
        self.sizes = data[:3]
        self.colors = ['yellowgreen', 'red', 'lightskyblue']
        self.patches, self.texts = plt.pie(self.sizes, explode=(0.05, 0.05, 0.05), colors=self.colors, shadow=True, startangle=90)

        plt.legend(self.patches, self.labels, loc='best')
        plt.axis('equal')
        plt.tight_layout()
        plt.savefig(path.join(path.dirname(__file__), 'SENTIMENT_DIAGRAMS/sentiment_analysis_of_'+data[3]+'_tweets.png'), transparent=True)
        plt.close()
        return
