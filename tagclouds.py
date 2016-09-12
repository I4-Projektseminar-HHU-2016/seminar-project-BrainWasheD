from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

class tagCloud(object):
    def __init__(self):
        return

    #Takes the results from wordpairs and creates a fitting wordcluster/cloud and saves it into WORDPAIRS
    def create_Cloud(self, data):
        print ('creating wordpair graph...')
        self.twitter_mask = np.array(Image.open(path.join(path.dirname(__file__), 'MASK/twitter_mask.png')))
        for word in data:
            wordcloud = WordCloud(font_path=path.join(path.dirname(__file__), 'FONT/CabinSketch-Bold.ttf'), relative_scaling=.5, width=1800, height=1400, stopwords=None, mask=self.twitter_mask)
            wordcloud.generate_from_frequencies(list(data[word].items()))
            wordcloud.to_file(path.join(path.dirname(__file__), 'WORDPAIRS/'+word+'.png'))            
        
        return

#Wordcloud by amueller on https://github.com/amueller/word_cloud
#Mask and Font found on http://sebastianraschka.com/Articles/2014_twitter_wordcloud.html
