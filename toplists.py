import nltk
from nltk import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer

class freq_Distributor():
    def __init__(self):
        return

    def frequency(self, modus, lang, *args):

        print ('creating toplists...')

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

        self.retok = nltk.RegexpTokenizer('\w+|\#?\w+|\@\w+')

        self.full_words = []
        self.freq= []
        self._fullString = ''

        self.rotate = {
                        'en' : self.en_freq,
                        'en-gb' : self.en_freq,
                        'de' : self.de_freq,
                        'fr' : self.fr_freq,
                        'es' : self.es_freq,
                        'ru' : self.ru_freq,
                        'fi' : self.fi_freq,
                        'no' : self.no_freq,
                        'sv' : self.sv_freq,
                        'nl' : self.nl_freq,
                        'it' : self.it_freq
        }

        for dicts in args:

            self.lg = ''
            self._String = ''

            for elem in dicts:
                
                self.temps = []
                self.lg = lang[elem]

                if modus == 'remove_hashtag':
                    for word in dicts[elem]:
                        if word != 's':
                            self.temps.append(word.replace('#', ''))

                elif modus == 'keep_hashtag':
                    for word in dicts[elem]:
                        if word != 's':
                            self.temps.append(word)

                self.temp_String = ' '.join(self.temps)
                self._String = self._String + ' ' + self.temp_String


            if self.lg in ['en', 'en-gb', 'de', 'fr', 'es', 'ru', 'fi', 'no', 'sv', 'nl', 'it']:
                self.words = self.retok.tokenize(self._String)
                self.words = [x for x in self.words if x != 's']
                self.words = [x for x in self.words if x != 'of']
                self.rotate[self.lg] = FreqDist(self.words).most_common(25)
                self.full_words.append(self.words)


        for elem in self.full_words:
            self.temp_fullString = ' '.join(elem)
            self._fullString = self._fullString + ' ' + self.temp_fullString
        self.freq = self.retok.tokenize(self._fullString)
        self.freq = [x for x in self.freq if x != 's']
        self.freq = [x for x in self.freq if x != 'of']
        self.full_freq = FreqDist(self.freq).most_common(25)
        
        return [self.full_freq, self.en_freq, self.de_freq, self.fr_freq, self.es_freq, self.ru_freq, 
                self.fi_freq, self.no_freq, self.sv_freq, self.nl_freq, self.it_freq]
