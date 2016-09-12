from collections import Counter, OrderedDict

class word_pairs():
    def __init__(self):
        return

    #Takes the Toplist and full texts to start netting the words together
    #So far it counts all Words that are together in tweets with the respective Topword
    def pairings(self, given_words, texts):
        print ('pairing words...')
        self.pairs = {}
        for word in given_words:
            self.elems = {}
            self.mc = []
            self.temp_words = []
            for text in texts.values():
                if (str(word[0]) in text) or ('#'+str(word[0]) in text):
                    for elem in text:
                        if (elem != str(word[0])) and (elem != ('#'+str(word[0]))):
                            self.temp_word = str(elem).replace('#', '')
                            self.temp_words.append(self.temp_word)
            self.mc = Counter(self.temp_words).most_common(75)
            for element in self.mc:
                self.elems[element[0]] = element[1] 
            self.elems = OrderedDict(sorted(self.elems.items(), key=lambda t: t[1], reverse=True))
            self.pairs[word[0]] = self.elems
        return self.pairs
