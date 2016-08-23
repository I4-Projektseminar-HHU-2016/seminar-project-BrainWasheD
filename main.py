from data_Reader import CSVDataReader
from timeline import TimelineCreator

if __name__ == "__main__":
        # text_Data, lang_Data, tweets_per_hour, unique_tweet, coordinates
        csv_reader = CSVDataReader()
        data_set_list = csv_reader.FileReader('result.csv')

        for elem in data_set_list[4]:
                print (elem)

        #timelines = TimelineCreator(data_set_list[2], data_set_list[1])
        #timelines.timeline()
