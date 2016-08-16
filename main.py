from data_Reader import CSVDataReader

if __name__ == "__main__":
        # text_Data, tweets_per_hour, tweets_per_day, unique_tweet
        csv_reader = CSVDataReader()
        data_set_list = csv_reader.FileReader('result.csv')
        print(data_set_list[3])
