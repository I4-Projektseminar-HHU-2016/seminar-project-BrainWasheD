from data_Reader import CSVDataReader
from timeline import TimelineCreator
from stopwords import filter_Stopwords
from toplists import freq_Distributor

if __name__ == "__main__":
        
        csv_reader = CSVDataReader()
        timelines = TimelineCreator()
        stops = filter_Stopwords()
        tops = freq_Distributor()

        # text_Data, lang_Data, tweets_per_hour, unique_tweet, coordinates
        data_set_list = csv_reader.FileReader('result.csv')
        
        #timelines.timeline(data_set_list[2])

        # List of Lists: full, english, german, french, spanish, russian, finnish, norwegian, swedisch, dutch, italian
        # Each List has: full text without stopwords, hashtags, mentions, keywords only
        filtered_data_list = stops.remove_Stopwords(data_set_list[0], data_set_list[1])
        
        undivided_toplist = tops.frequency(data_set_list[1], filtered_data_list[1][0], filtered_data_list[2][0], filtered_data_list[3][0], filtered_data_list[4][0], filtered_data_list[5][0], filtered_data_list[6][0], filtered_data_list[7][0], filtered_data_list[8][0], filtered_data_list[9][0], filtered_data_list[10][0])
        hashtag_toplist = tops.frequency(data_set_list[1], filtered_data_list[1][1], filtered_data_list[2][1], filtered_data_list[3][1], filtered_data_list[4][1], filtered_data_list[5][1], filtered_data_list[6][1], filtered_data_list[7][1], filtered_data_list[8][1], filtered_data_list[9][1], filtered_data_list[10][1])
        mention_toplist = tops.frequency(data_set_list[1], filtered_data_list[1][2], filtered_data_list[2][2], filtered_data_list[3][2], filtered_data_list[4][2], filtered_data_list[5][2], filtered_data_list[6][2], filtered_data_list[7][2], filtered_data_list[8][2], filtered_data_list[9][2], filtered_data_list[10][2])
        keyword_toplist = tops.frequency(data_set_list[1], filtered_data_list[1][3], filtered_data_list[2][3], filtered_data_list[3][3], filtered_data_list[4][3], filtered_data_list[5][3], filtered_data_list[6][3], filtered_data_list[7][3], filtered_data_list[8][3], filtered_data_list[9][3], filtered_data_list[10][3])

        print (keyword_toplist[0])
