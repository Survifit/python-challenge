import os
import csv

polls_csv = os.path.join("election_data.csv")
voterDict = {}
votesDict = {}

with open(polls_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    for row in csvreader:
        if row[0] in voterDict:
            voterDict[row[0]] = voterDict[row[0]] + 1
        else:
            voterDict[row[0]] = 1

        if row[2] in votesDict:
            votesDict[row[2]] = votesDict[row[2]] + 1
        else:
            votesDict[row[2]] = 1


too_many = [key for key, value in voterDict.items() if value > 1]

print(too_many)

for key, value in votesDict.items():
    print(f"{key} had {value} votes.")


