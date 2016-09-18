from data_Reader import CSVDataReader
from timeline import TimelineCreator
from stopwords import filter_Stopwords
from toplists import freq_Distributor
from wordpairs import word_pairs
from tagclouds import tagCloud
from sentiment import sentAna
from senti_diagram import sentimentDiagram
from percentages import percs
import unicodecsv as csv
from collections import Counter
from toplist_graph import topGraph
if __name__ == "__main__":


        #Creating instances of the several classes
        csv_reader = CSVDataReader()
        timelines = TimelineCreator()
        stops = filter_Stopwords()
        tops = freq_Distributor()
        pairs = word_pairs()
        cloud = tagCloud()
        senti = sentAna()
        sd = sentimentDiagram()
        prc = percs()
        tg = topGraph()

        # text_Data, lang_Data, tweets_per_hour, unique_tweet, coordinates
        data_set_list = csv_reader.FileReader('result.csv')
        timelines.timeline(data_set_list[2])

        # List of Lists: full, english, german, french, spanish, russian, finnish, norwegian, swedisch, dutch, italian
        # Each List has: full text without stopwords, hashtags, mentions, keywords only
        filtered_data_list = stops.remove_Stopwords(data_set_list[0], data_set_list[1])

        #full_freq, en_freq, de_freq, fr_freq, es_freq, ru_freq, fi_freq, no_freq, sv_freq, nl_freq, it_freq
        undivided_toplist = tops.frequency('remove_hashtag', data_set_list[1], filtered_data_list[0][0])
        hashtag_toplist = tops.frequency('keep_hashtag', data_set_list[1], filtered_data_list[0][1])
        mention_toplist = tops.frequency('keep_hashtag', data_set_list[1], filtered_data_list[0][2])
        keyword_toplist = tops.frequency('keep_hashtag', data_set_list[1], filtered_data_list[0][3])

        tg.graph([undivided_toplist[0], hashtag_toplist[0], keyword_toplist[0]],
                ['unfiltered', 'hashtags', 'keywords'])

        
        #Percentage of Mentions compared to all tweets
        prc.percent(filtered_data_list[0][0], mention_toplist[0])

        #Creating the Wordpairs
        pairings = pairs.pairings(undivided_toplist[0], filtered_data_list[0][0])

        with open('plotly.csv', 'ab') as resultFile:
            writer = csv.writer(resultFile, delimiter=";", lineterminator="\r\n", encoding='utf-8')
            for tag in undivided_toplist[0]:
                (key, value) = tag
                writer.writerow([tag, pairings[key]])
        
        #Creating the worpairgraphs
        cloud.create_Cloud(pairings)

        #Sentimentanalysis
        en_senti = senti.analyze(filtered_data_list[1][0], 'en')
        de_senti = senti.analyze(filtered_data_list[2][0], 'de')
        es_senti = senti.analyze(filtered_data_list[4][0], 'es')
        all_senti = [en_senti[0]+de_senti[0]+es_senti[0], en_senti[1]+de_senti[1]+es_senti[1], en_senti[2]+de_senti[2]+es_senti[2], 'all']
        
        #Creating the graphs of the sentiment analysis
        sd.diagram(en_senti)
        sd.diagram(de_senti)
        sd.diagram(es_senti)
        sd.diagram(all_senti)
