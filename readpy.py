import csv
with open('./LR5-SSR_2025-07-19_H11_M07_S01.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        print(', '.join(row))
