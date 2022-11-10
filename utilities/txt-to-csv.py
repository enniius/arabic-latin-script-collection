# read a txt file and write it in csv file

import csv

with open('./countries/tunisia/filtered/CTAB.txt', 'r', encoding = "ISO-8859-1") as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('CTAB1.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(lines)
