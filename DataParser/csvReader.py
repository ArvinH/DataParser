import csv
import urllib.request
import json

class csvReader:
    def __init__(self, filesrc):
        self.filesrc = filesrc
    def readCSV(self):
        
        rfile = open(self.filesrc,'r',encoding='utf-8', newline='')
        wfile = open(self.filesrc,'r',encoding='utf-8', newline='')
        csvR = csv.reader(rfile)
        for row in csvR:
             print(','.join(row))
        
def main():
    r = csvReader('../data_csv/data_time.csv')
    r.readCSV()



if __name__ == '__main__':
    main()
