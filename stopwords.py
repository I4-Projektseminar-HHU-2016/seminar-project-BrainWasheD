import re
from nltk.corpus import stopwords

class filter_Stopwords():
    def __init__(self):
        return

    def remove_Stopwords(self, text, lang):

        self.full_Text = {}
        self.en_Text = {}
        self.de_Text = {}
        self.fr_Text = {}
        self.es_Text = {}
        self.ru_Text = {}
        
        
        self.replaces = ["'re", "'ve", "'ll", "'m", "'d", "'s", "'t", "<",
                        ">", ",", ".", "-", "_", ";", ":", "+", "*", "~",
                        "!", "?", "|", "(", ")", "https//", "http//"]

        self.en_Stops = set(stopwords.words('english'))
        self.de_Stops = set(stopwords.words('german'))
        self.fr_Stops = set(stopwords.words('french'))
        self.es_Stops = set(stopwords.words('spanish'))
        self.ru_Stops = set(stopwords.words('russian'))

        for elem in text:

            self.temp = []
    
            text[elem] = re.sub(r"(?i)\b((?:http?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?]))", '', text[elem])
            for obj in self.replaces:
                text[elem] = text[elem].replace(obj, '')
                
            if lang[elem] == 'en':
                
                for word in text[elem].split():
                    if word not in self.en_Stops and len(word) > 1:
                        self.temp.append(word)
                self.full_Text[elem] = self.temp
                self.en_Text[elem] = self.temp
                print (self.en_Text[elem])
                
            elif lang[elem] == 'de':
                
                for word in text[elem].split():
                    if word not in self.de_Stops and len(word) > 1:
                        self.temp.append(word)
                self.full_Text[elem] = self.temp
                self.de_Text[elem] = self.temp
                
            elif lang[elem] == 'fr':
                
                for word in text[elem].split():
                    if word not in self.fr_Stops and len(word) > 1:
                        self.temp.append(word)
                self.full_Text[elem] = self.temp
                self.fr_Text[elem] = self.temp
                
            elif lang[elem] == 'es':
                
                for word in text[elem].split():
                    if word not in self.es_Stops and len(word) > 1:
                        self.temp.append(word)
                self.full_Text[elem] = self.temp
                self.es_Text[elem] = self.temp
                
            elif lang[elem] == 'ru':
                
                for word in text[elem].split():
                    if word not in self.ru_Stops and len(word) > 1:
                        self.temp.append(word)
                self.full_Text[elem] = self.temp
                self.ru_Text[elem] = self.temp
                
            else:
                print ('undefined')

        return [self.full_Text, self.en_Text, self.de_Text, self.fr_Text, self.es_Text, self.ru_Text]

    
