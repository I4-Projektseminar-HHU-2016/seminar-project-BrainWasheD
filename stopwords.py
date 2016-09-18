import re
from nltk.corpus import stopwords

class filter_Stopwords():
    def __init__(self):
        return

    # Returns lists of Dictionaries with their respective language
    def remove_Stopwords(self, text, lang):

        print ('applying stopwordfilters...')

        #Several Dictionaries to save the texts in different languages

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

        
        self.replaces = ["'re", "'ve", "'ll", "'m", "'t", "d'", "<", "]",
                        "[", ">", ",", ".", ";", "+", "*", "~", "&amp", '"', 
                        "!", "?", "|", "(", ")", ":"]

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

        #Dictionary containing the Stopwordlists of the languages
        self.rotate = {
                        'en' : self.en_Stops,
                        'en-gb' : self.en_Stops,
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

        self.rotate_two = {
                        'en' : [self.en_Text, self.en_Hashtag, self.en_Mentions, self.en_Stripped],
                        'en-gb' : [self.en_Text, self.en_Hashtag, self.en_Mentions, self.en_Stripped],
                        'de' : [self.de_Text, self.de_Hashtag, self.de_Mentions, self.de_Stripped],
                        'fr' : [self.fr_Text, self.fr_Hashtag, self.fr_Mentions, self.fr_Stripped],
                        'es' : [self.es_Text, self.es_Hashtag, self.es_Mentions, self.es_Stripped],
                        'ru' : [self.ru_Text, self.ru_Hashtag, self.ru_Mentions, self.ru_Stripped],
                        'fi' : [self.fi_Text, self.fi_Hashtag, self.fi_Mentions, self.fi_Stripped],
                        'no' : [self.no_Text, self.no_Hashtag, self.no_Mentions, self.no_Stripped],
                        'sv' : [self.sv_Text, self.sv_Hashtag, self.sv_Mentions, self.sv_Stripped],
                        'nl' : [self.nl_Text, self.nl_Hashtag, self.nl_Mentions, self.nl_Stripped],
                        'it' : [self.it_Text, self.it_Hashtag, self.it_Mentions, self.it_Stripped]
        }

        for elem in text:

            self.temp = []
            self.stripped = []
            self.hashtags = []
            self.mentions = []
    
            text[elem] = re.sub(r'https://\S+', '', text[elem])
            for obj in self.replaces:
                text[elem] = text[elem].replace(obj, '')

            #splitting the words into keywords, mentions and hashtags
            for word in text[elem].split():
                if (lang[elem] in ['en', 'en-gb', 'de', 'fr', 'es', 'ru', 'fi', 'no', 'sv', 'nl', 'it']):
                    if ((word not in self.rotate[lang[elem]]) and (len(word) > 1) and (word != 's') and (word != 'rt') and (word != "it's")):
                        self.temp.append(word)
                        if re.match('#(\w+)', word):
                            self.hashtags.append(word)
                        elif re.match('(?<=^|(?<=[^a-zA-Z0-9-\.]))@([A-Za-z0-9_]+)', word):
                            self.mentions.append(word)
                        else:
                            self.stripped.append(word)

            self.temp = [x for x in self.temp if x != 's']

            #Saving the Data into the respective dictionaries

            if lang[elem] in ['en', 'en-gb', 'de', 'fr', 'es', 'ru', 'fi', 'no', 'sv', 'nl', 'it']:
                
                self.rotate_two[lang[elem]][0] = self.temp
                self.rotate_two[lang[elem]][1] = self.hashtags
                if not len(self.mentions) == 0:
                    self.rotate_two[lang[elem]][2] = self.mentions
                self.rotate_two[lang[elem]][3] = self.stripped


            self.full_Text[elem] = self.temp
            self.full_Hashtag[elem] = self.hashtags
            self.full_Mentions[elem] = self.mentions
            self.full_Stripped[elem] = self.stripped

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

    
