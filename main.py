from data_Reader import CSVDataReader

if __name__ == "__main__":
        csv_reader = CSVDataReader([], [], 0, {}, {})
        csv_reader.FileReader('result.csv')
        print(csv_reader.unique_tweets)
