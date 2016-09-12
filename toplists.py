import nltk
from nltk import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer

class freq_Distributor():
    def __init__(self):
        return

    def frequency(self, modus, lang, *args):

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

        self.full_words = []
        self.freq= []
        self._fullString = ''

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


            if self.lg == 'en':
                self.words = self.retok.tokenize(self._String)
                self.words = [x for x in self.words if x != 's']
                self.words = [x for x in self.words if x != 'of']
                self.en_freq = FreqDist(self.words).most_common(25)
                self.full_words.append(self.words)

            elif self.lg == 'de':
                self.words = self.retok.tokenize(self._String)
                self.words = [x for x in self.words if x != 's']
                self.words = [x for x in self.words if x != 'of']
                self.de_freq = FreqDist(self.words).most_common(25)                
                self.full_words.append(self.words)

            elif self.lg == 'fr':
                self.words = self.retok.tokenize(self._String)
                self.words = [x for x in self.words if x != 's']
                self.words = [x for x in self.words if x != 'of']
                self.fr_freq = FreqDist(self.words).most_common(25)
                self.full_words.append(self.words)

            elif self.lg == 'es':
                self.words = self.retok.tokenize(self._String)
                self.words = [x for x in self.words if x != 's']
                self.words = [x for x in self.words if x != 'of']
                self.es_freq = FreqDist(self.words).most_common(25)
                self.full_words.append(self.words)

            elif self.lg == 'ru':
                self.words = self.retok.tokenize(self._String)
                self.words = [x for x in self.words if x != 's']
                self.words = [x for x in self.words if x != 'of']
                self.ru_freq = FreqDist(self.words).most_common(25)
                self.full_words.append(self.words)

            

            elif self.lg == 'fi':
                self.words = self.retok.tokenize(self._String)
                self.words = [x for x in self.words if x != 's']
                self.words = [x for x in self.words if x != 'of']
                self.fi_freq = FreqDist(self.words).most_common(25)
                self.full_words.append(self.words)

            elif self.lg == 'no':
                self.words = self.retok.tokenize(self._String)
                self.words = [x for x in self.words if x != 's']
                self.words = [x for x in self.words if x != 'of']
                self.no_freq = FreqDist(self.words).most_common(25)
                self.full_words.append(self.words)

            elif self.lg == 'sv':
                self.words = self.retok.tokenize(self._String)
                self.words = [x for x in self.words if x != 's']
                self.words = [x for x in self.words if x != 'of']
                self.sv_freq = FreqDist(self.words).most_common(25)
                self.full_words.append(self.words)

            elif self.lg == 'nl':
                self.words = self.retok.tokenize(self._String)
                self.words = [x for x in self.words if x != 's']
                self.words = [x for x in self.words if x != 'of']
                self.nl_freq = FreqDist(self.words).most_common(25)
                self.full_words.append(self.words)

            elif self.lg == 'it':
                self.words = self.retok.tokenize(self._String)
                self.words = [x for x in self.words if x != 's']
                self.words = [x for x in self.words if x != 'of']
                self.it_freq = FreqDist(self.words).most_common(25)
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
