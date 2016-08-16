import numpy as np
import matplotlib.pyplot as plt

class TimelineCreator():

        def __init__(self, days, hours):
                self.hours = hours
                self.days = days
                return

        # A simple line-style graph for the timeline
        def timeline(self):
                self.dicts = [self.days, self.hours]
                self.labels = ['days', 'daytime in hours']
                self.x = 0
                for elem in self.dicts:
        
                        self.index = np.arange(len(elem))
                        self.names = elem.keys()
                        self.values = np.array([float(v) for v in elem.values()])
                        plt.plot(self.index, self.values, 'r-')
                        plt.xticks(self.index, self.names, rotation = 15)
                        plt.xlabel(self.labels[self.x])
                        plt.ylabel('Amount')
                        plt.show()

                        self.x += 1
                return


