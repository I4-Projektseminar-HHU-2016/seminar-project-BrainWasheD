from data_Reader import CSVDataReader
from timeline import TimelineCreator
from stopwords import filter_Stopwords

if __name__ == "__main__":
        # text_Data, lang_Data, tweets_per_hour, unique_tweet, coordinates
        csv_reader = CSVDataReader()
        data_set_list = csv_reader.FileReader('result.csv')
        stops = filter_Stopwords()

        # full_Text, en_Text, de_Text, fr_Text, es_Text, ru_Text
        filtered_data_list = stops.remove_Stopwords(data_set_list[0], data_set_list[1])
        #print (filtered_data_list[2])

        
        #for elem in data_set_list[4]:
        #        print (elem)

        #timelines = TimelineCreator(data_set_list[2], data_set_list[1])
        #timelines.timeline()
