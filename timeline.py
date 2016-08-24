import numpy as np
import matplotlib.pyplot as plt

class TimelineCreator():

        def __init__(self):
                return

        # A simple line-style graph for the timeline
        def timeline(self, hours):
                
                self.x = 0

                self.index = np.arange(len(hours))
                self.names = hours.keys()
                self.values = np.array([float(v) for v in hours.values()])
                plt.plot(self.index, self.values, 'r-')
                plt.xticks(self.index, self.names, rotation = 15)
                plt.xlabel('Time of Day')
                plt.ylabel('Amount')
                plt.show()

                self.x += 1
                
                return


