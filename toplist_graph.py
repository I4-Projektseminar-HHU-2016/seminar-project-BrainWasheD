import matplotlib.pyplot as plt
import numpy as np
from os import path
from matplotlib import cm

class topGraph(object):
    def __init__(self):
        return

    def graph(self, toplists, names):

        self.colors = cm.Set1(np.arange(25)/25.)
        self.index = 0

        for toplist in toplists:
            self.labels = []
            self.amounts = []
            
            self.fig = plt.figure(1)
            self.ax = self.fig.add_subplot(111)
            
            for elem in toplist:
                (self.key, self.value) = elem
                self.labels.append(self.key)
                self.amounts.append(self.value)

            self.y_pos = np.arange(len(self.labels))

            self.graph = plt.barh(self.y_pos, self.amounts, alpha = 0.4, height = 0.95, color = self.colors)
            plt.yticks(self.y_pos+0.5, self.labels)
            plt.xlabel('Amount')
            plt.title('Top 25 '+names[self.index])

            self.fig.savefig(path.join(path.dirname(__file__), 'TOPLISTS/'+names[self.index]+'.png'), transparent=True, bbox_inches='tight')

            plt.close()

            self.index += 1
        
        return
