class sentAna(object):
    def __init__(self):
        return

    #Takes lists of positive and negative Terms and their variations
    #Compares it with the words in the tweets and counts positive and negative words to compare against
    #More positive words than negative ones means the tweet tends to be positive
    def analyze(self, data, lang):

        print ('calculating sentiment...')
        
        self.pos_Count = 0
        self.neg_Count = 0
        self.neut_Count = 0
        for elem in data.values():
            self.pos_Count_Sent = 0
            self.neg_Count_Sent = 0
            for word in elem:
                if word.lower() in open('SENTIMENT_WORDLISTS/pos-words_'+lang+'.txt').read():
                    self.pos_Count_Sent += 1
                elif word.lower() in open('SENTIMENT_WORDLISTS/neg-words_'+lang+'.txt').read():
                    self.neg_Count_Sent += 1

            if self.pos_Count_Sent > self.neg_Count_Sent:
                self.pos_Count += 1
            elif self.neg_Count_Sent > self.pos_Count_Sent:
                self.neg_Count += 1
            elif self.pos_Count_Sent == self.neg_Count_Sent:
                self.neut_Count += 1

        return [self.pos_Count, self.neg_Count, self.neut_Count, lang]
