import unicodecsv as csv
from collections import Counter, OrderedDict


class CSVDataReader():

        def __init__(self):
                return
        def FileReader(self, fileName):

                self.temp_id = []
                self.temp_datelist = []
                self.temp_time_of_day = []

                self.raw_Data = []
                self.text_Data = []

                self.unique_tweets = 0

                self.tweets_per_hour = {}
                self.tweets_per_day = {}
        
                
                with open(fileName, 'rb') as data:
                        reader = csv.reader(data, delimiter=";", lineterminator="\r\n", encoding='utf-8')
                        
                        # Die csv Datei wird Zeile fuer Zeile eingelesen und aufs Datum 
                        # geprueft um die relevanten Daten zu filtern
                        for row in reader:

                                self.split_date = row[1].split() # Trennung von Datum und Uhrzeit
                                self.check_date = self.split_date[0].split('-') # Jahr, Monat und Tag aufbrechen
                                
                                if ((row[0] not in self.temp_id)
                                        and (self.check_date[0] == '2016')
                                        and (self.check_date[1] == '08' or self.check_date[1] == '09')):
                                        
                                        self.temp_id.append(row[0])
                                        self.unique_tweets += 1
                                        
                                        self.raw_Data.append(row) # Zeile der CSV in die Liste gepackt
                                        self.text_Data.append(row[2]) # Text in Liste speichern
			
                                        self.check_date.remove(self.check_date[0]) # Jahr wird entfernt
                                        self.check_date = '-'.join(self.check_date) # Monat/ Tag zu String
                                        self.temp_datelist.append(self.check_date) # neues Format in Liste gepackt
			
                                        self.new_time = self.split_date[1].split(':') # Stunden, Min. und Sek. aufbrechen
                                        self.temp_time_of_day.append(self.new_time[0]) # Nur Stunden gespeichert
                                                
                        self.tweets_per_hour = Counter(self.temp_time_of_day) # Zaehlen der tweets je Stunde
                        self.tweets_per_hour = OrderedDict(sorted(self.tweets_per_hour.items(), key=lambda t: t[0]))
                        self.tweets_per_day = Counter(self.temp_datelist) # Zaehlen der tweets je Tag
                        self.tweets_per_day = OrderedDict(sorted(self.tweets_per_day.items(), key=lambda t: t[0]))
                        data.close()
                return [self.text_Data, self.tweets_per_hour, self.tweets_per_day, self.unique_tweets]
