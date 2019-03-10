import os
import csv

polls_csv = os.path.join("election_data.csv")


with open(polls_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    votes = [row[2] for row in csvreader]
        

candidates = list(set(votes))
print(votes.count('Khan'))
for candidate in candidates:
    #print(candidate)
    print(f"{candidate} had a total of {votes.count(candidate)} votes.")





