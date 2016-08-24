import re
from nltk.corpus import stopwords

class filter_Stopwords():
    def __init__(self):
        return

    def remove_Stopwords(self, text, lang):

        self.full_Text, self.full_Hashtag, self.full_Mentions, self.full_Stripped = {}, {}, {}, {}
        
        self.en_Text, self.en_Hashtag, self.en_Mentions, self.en_Stripped = {}, {}, {}, {}
        self.de_Text, self.de_Hashtag, self.de_Mentions, self.de_Stripped = {}, {}, {}, {}
        self.fr_Text, self.fr_Hashtag, self.fr_Mentions, self.fr_Stripped = {}, {}, {}, {}
        self.es_Text, self.es_Hashtag, self.es_Mentions, self.es_Stripped = {}, {}, {}, {}
        self.ru_Text, self.ru_Hashtag, self.ru_Mentions, self.ru_Stripped = {}, {}, {}, {}

        self.fi_Text, self.fi_Hashtag, self.fi_Mentions, self.fi_Stripped = {}, {}, {}, {}
        self.no_Text, self.no_Hashtag, self.no_Mentions, self.no_Stripped = {}, {}, {}, {}
        self.sv_Text, self.sv_Hashtag, self.sv_Mentions, self.sv_Stripped = {}, {}, {}, {}
        self.nl_Text, self.nl_Hashtag, self.nl_Mentions, self.nl_Stripped = {}, {}, {}, {}
        self.it_Text, self.it_Hashtag, self.it_Mentions, self.it_Stripped = {}, {}, {}, {}

        
        self.replaces = ["'re", "'ve", "'ll", "'m", "'d", "'s", "'t", "<",
                        ">", ",", ".", "-", "_", ";", ":", "+", "*", "~",
                        '"', "!", "?", "|", "(", ")", "https//", "http//"]

        self.en_Stops = set(stopwords.words('english'))
        self.de_Stops = set(stopwords.words('german'))
        self.fr_Stops = set(stopwords.words('french'))
        self.es_Stops = set(stopwords.words('spanish'))
        self.ru_Stops = set(stopwords.words('russian'))

        self.fi_Stops = set(stopwords.words('finnish'))
        self.no_Stops = set(stopwords.words('norwegian'))
        self.sv_Stops = set(stopwords.words('swedish'))
        self.nl_Stops = set(stopwords.words('dutch'))
        self.it_Stops = set(stopwords.words('italian'))

        self.rotate = {
                        'en' : self.en_Stops,
                        'de' : self.de_Stops,
                        'fr' : self.fr_Stops,
                        'es' : self.es_Stops,
                        'ru' : self.ru_Stops,
                        'fi' : self.fi_Stops,
                        'no' : self.no_Stops,
                        'sv' : self.sv_Stops,
                        'nl' : self.nl_Stops,
                        'it' : self.it_Stops
        }

        for elem in text:

            self.temp = []
            self.stripped = []
            self.hashtags = []
            self.mentions = []
    
            text[elem] = re.sub(r"(?i)\b((?:http?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?]))", '', text[elem])
            for obj in self.replaces:
                text[elem] = text[elem].replace(obj, '')


            for word in text[elem].split():
                if (lang[elem] in ['en', 'de', 'fr', 'es', 'ru', 'fi', 'no', 'sv', 'nl', 'it']):
                    if ((word not in self.rotate[lang[elem]]) and (len(word) > 1)):
                        self.temp.append(word)
                        if re.match('#(\w+)', word):
                            self.hashtags.append(word)
                        elif re.match('(?<=^|(?<=[^a-zA-Z0-9-\.]))@([A-Za-z0-9_]+)', word):
                            self.mentions.append(word)
                        else:
                            self.stripped.append(word)
                            
                self.full_Text[elem] = self.temp
                self.full_Hashtag[elem] = self.hashtags
                self.full_Mentions[elem] = self.mentions
                self.full_Stripped[elem] = self.stripped
            
                
                if lang[elem] == 'en':
                
                    self.en_Text[elem] = self.temp
                    self.en_Hashtag[elem] = self.hashtags
                    if not len(self.mentions) == 0:
                        self.en_Mentions[elem] = self.mentions
                    self.en_Stripped[elem] = self.stripped

                elif lang[elem] == 'en-gb':
                            
                    self.full_Text[elem] = self.temp
                    self.full_Hashtag[elem] = self.hashtags
                    self.full_Mentions[elem] = self.mentions
                    self.full_Stripped[elem] = self.stripped
                
                    self.en_Text[elem] = self.temp
                    self.en_Hashtag[elem] = self.hashtags
                    if not len(self.mentions) == 0:
                        self.en_Mentions[elem] = self.mentions
                    self.en_Stripped[elem] = self.stripped

                
                elif lang[elem] == 'de':
                
                    self.de_Text[elem] = self.temp
                    self.de_Hashtag[elem] = self.hashtags
                    if not len(self.mentions) == 0:
                        self.de_Mentions[elem] = self.mentions
                    self.de_Stripped[elem] = self.stripped
                
                elif lang[elem] == 'fr':

                    self.fr_Text[elem] = self.temp
                    self.fr_Hashtag[elem] = self.hashtags
                    if not len(self.mentions) == 0:
                        self.fr_Mentions[elem] = self.mentions
                    self.fr_Stripped[elem] = self.stripped
                
                elif lang[elem] == 'es':

                    self.es_Text[elem] = self.temp
                    self.es_Hashtag[elem] = self.hashtags
                    if not len(self.mentions) == 0:
                        self.es_Mentions[elem] = self.mentions
                    self.es_Stripped[elem] = self.stripped
                                 
                elif lang[elem] == 'ru':
                
                    self.ru_Text[elem] = self.temp
                    self.ru_Hashtag[elem] = self.hashtags
                    if not len(self.mentions) == 0:
                        self.ru_Mentions[elem] = self.mentions
                    self.ru_Stripped[elem] = self.stripped

                elif lang[elem] == 'fi':
                    
                    self.fi_Text[elem] = self.temp
                    self.fi_Hashtag[elem] = self.hashtags
                    if not len(self.mentions) == 0:
                        self.fi_Mentions[elem] = self.mentions
                    self.fi_Stripped[elem] = self.stripped

                elif lang[elem] == 'no':
                    
                    self.no_Text[elem] = self.temp
                    self.no_Hashtag[elem] = self.hashtags
                    if not len(self.mentions) == 0:
                        self.no_Mentions[elem] = self.mentions
                    self.no_Stripped[elem] = self.stripped

                elif lang[elem] == 'sv':
                
                    self.sv_Text[elem] = self.temp
                    self.sv_Hashtag[elem] = self.hashtags
                    if not len(self.mentions) == 0:
                        self.sv_Mentions[elem] = self.mentions
                    self.sv_Stripped[elem] = self.stripped

                elif lang[elem] == 'nl':
                
                    self.nl_Text[elem] = self.temp
                    self.nl_Hashtag[elem] = self.hashtags
                    if not len(self.mentions) == 0:
                        self.nl_Mentions[elem] = self.mentions
                    self.nl_Stripped[elem] = self.stripped

                elif lang[elem] == 'it':

                    self.it_Text[elem] = self.temp
                    self.it_Hashtag[elem] = self.hashtags
                    if not len(self.mentions) == 0:
                        self.it_Mentions[elem] = self.mentions
                    self.it_Stripped[elem] = self.stripped

        self.full = [self.full_Text, self.full_Hashtag, self.full_Mentions, self.full_Stripped]
        
        self.english = [self.en_Text, self.en_Hashtag, self.en_Mentions, self.en_Stripped]
        self.german = [self.de_Text, self.de_Hashtag, self.de_Mentions, self.de_Stripped]
        self.french = [self.fr_Text, self.fr_Hashtag, self.fr_Mentions, self.fr_Stripped]
        self.spanish = [self.es_Text, self.es_Hashtag, self.es_Mentions, self.es_Stripped]
        self.russian = [self.ru_Text, self.ru_Hashtag, self.ru_Mentions, self.ru_Stripped]

        self.finnish = [self.fi_Text, self.fi_Hashtag, self.fi_Mentions, self.fi_Stripped]
        self.norwegian = [self.no_Text, self.no_Hashtag, self.no_Mentions, self.no_Stripped]
        self.swedish = [self.sv_Text, self.sv_Hashtag, self.sv_Mentions, self.sv_Stripped]
        self.dutch = [self.nl_Text, self.nl_Hashtag, self.nl_Mentions, self.nl_Stripped]
        self.italian = [self.it_Text, self.it_Hashtag, self.it_Mentions, self.it_Stripped]

        return [self.full, self.english, self.german, self.french, self.spanish,
                self.russian, self.finnish, self.norwegian, self.swedish, self.dutch, self.italian]

    
