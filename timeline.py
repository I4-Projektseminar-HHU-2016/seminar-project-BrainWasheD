import numpy as np
import matplotlib.pyplot as plt
from os import path

class TimelineCreator():

    def __init__(self):
        return

    # A simple line-style graph for the timeline
    def timeline(self, hours):

        print ('creating timeline...')

        self.index = [int(x) for x in hours.keys()]
        self.values = [float(v) for v in hours.values()]
        self.avg = 0
        
        for x in self.values:
            self.avg += x
        self.avg = (self.avg/24)
        
        self.fig, self.ax = plt.subplots(1)
        self.ax.plot(self.index, self.values, 'k*', label = 'Tweets at hour X')
        self.ax.set_xlim(0, 23)
        self.ax.fill_between(self.index, 0, self.values, facecolor = 'black', alpha = '0.7')

        plt.axhline(y = self.avg, color = 'c', marker = '.', label = 'Average Tweets in an hour')
        
        plt.title('Tweet Timeline')
        plt.ylabel('Tweets')
        plt.xlabel('Time of Day')
        plt.legend(loc = 4)
        plt.xticks(np.arange(len(hours)), hours.keys(), rotation = 15)
        plt.savefig(path.join(path.dirname(__file__), 'RESULTS/timeline.png'), transparent=True)
        plt.close()
        
        return


