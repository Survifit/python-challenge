import os
import csv
from statistics import mean

budget_csv = os.path.join("budget_data.csv")
date = []
pandl = []

# Open and read csv
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csvreader:
        #print(row)
        date.append(row[0])
        pandl.append(int(row[1]))

#print(date)
#print(pandl)

print("Financial Analysis")
print("---------------------------------")
print(f"Total Months: {len(date)}")
print(f"Total: ${sum(pandl)}")
print(f"Average: ${round(mean(pandl),2)}")
maxDateIndex = pandl.index(max(pandl))
minDateIndex = pandl.index(min(pandl))
print(f"Greatest Increase in Profits: {date[maxDateIndex]} (${max(pandl)})")
print(f"Greatest Decrease in Profits: {date[minDateIndex]} (${min(pandl)})")
print(maxDateIndex)
print(minDateIndex)
print(date[maxDateIndex])



