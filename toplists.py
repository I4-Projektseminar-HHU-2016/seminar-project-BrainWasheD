import six
import itertools
import nltk
from nltk import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer

class freq_Distributor():
    def __init__(self):
        return

    def frequency(self, lang, *args):

        self.full_freq = []

        self.en_freq = []
        self.de_freq = []
        self.fr_freq = []
        self.es_freq = []
        self.ru_freq = []
        
        self.fi_freq = []
        self.no_freq = []
        self.sv_freq = []
        self.nl_freq = []
        self.it_freq = []

        self.retok = nltk.RegexpTokenizer('\w+|\#?\w+|\@?\w+')

        for dicts in args:

            self.lg = ''
            self._String = ''

            for elem in dicts:

                self.lg = lang[elem]

                self.temp_String = ' '.join(dicts[elem])
                self._String = self._String + self.temp_String


            if self.lg == 'en':
                self.words = self.retok.tokenize(self._String)
                self.en_freq = FreqDist(self.words).most_common(25)
                self.full_freq = FreqDist(self.words).most_common(25)

            elif self.lg == 'de':
                self.words = self.retok.tokenize(self._String)
                self.de_freq = FreqDist(self.words).most_common(25)                
                self.full_freq = FreqDist(self.words).most_common(25)

            elif self.lg == 'fr':
                self.words = self.retok.tokenize(self._String)
                self.fr_freq = FreqDist(self.words).most_common(25)
                self.full_freq = FreqDist(self.words).most_common(25)

            elif self.lg == 'es':
                self.words = self.retok.tokenize(self._String)
                self.es_freq = FreqDist(self.words).most_common(25)
                self.full_freq = FreqDist(self.words).most_common(25)

            elif self.lg == 'ru':
                self.words = self.retok.tokenize(self._String)
                self.ru_freq = FreqDist(self.words).most_common(25)
                self.full_freq = FreqDist(self.words).most_common(25)

            

            elif self.lg == 'fi':
                self.words = self.retok.tokenize(self._String)
                self.fi_freq = FreqDist(self.words).most_common(25)
                self.full_freq = FreqDist(self.words).most_common(25)

            elif self.lg == 'no':
                self.words = self.retok.tokenize(self._String)
                self.no_freq = FreqDist(self.words).most_common(25)
                self.full_freq = FreqDist(self.words).most_common(25)

            elif self.lg == 'sv':
                self.words = self.retok.tokenize(self._String)
                self.sv_freq = FreqDist(self.words).most_common(25)
                self.full_freq = FreqDist(self.words).most_common(25)

            elif self.lg == 'nl':
                self.words = self.retok.tokenize(self._String)
                self.nl_freq = FreqDist(self.words).most_common(25)
                self.full_freq = FreqDist(self.words).most_common(25)

            elif self.lg == 'it':
                self.words = self.retok.tokenize(self._String)
                self.it_freq = FreqDist(self.words).most_common(25)
                self.full_freq = FreqDist(self.words).most_common(25)
        
        return [self.full_freq, self.en_freq, self.de_freq, self.fr_freq, self.es_freq, self.ru_freq, 
                self.fi_freq, self.no_freq, self.sv_freq, self.nl_freq, self.it_freq]
