from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud

class tagCloud(object):
    def __init__(self):
        return

    def create_Cloud(self, data):

        for word in data:
            wordcloud = WordCloud(max_font_size=200, relative_scaling=.5, width=1280, height=800, stopwords=None)
            wordcloud.generate_from_frequencies(list(data[word].items()))
            wordcloud.to_file(path.join(path.dirname(__file__), word+'.png'))
            
        
        return
