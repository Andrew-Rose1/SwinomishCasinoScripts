import os
import csv

path = 'C:\\Users\\arose\\Programs\\MicrosoftVersionCSV'

file = open(path, "r")
reader = csv.reader(file, delimiter=',')
for row in reader:
    print(col[4])
