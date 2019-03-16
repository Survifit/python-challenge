import os
import csv
from statistics import mean
import numpy as np

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
        pandl.append(float(row[1]))

pandlDiff = np.diff(pandl)
maxDateIndex = np.where(pandlDiff == max(pandlDiff))
minDateIndex = np.where(pandlDiff == min(pandlDiff))

print("Financial Analysis")
print("---------------------------------")
print(f"Total Months: {len(date)}")
print(f"Total: ${int(sum(pandl))}")
print(f"Average Change: ${round(mean(pandlDiff),2)}")
print(f"Greatest Increase in Profits: {date[int(maxDateIndex[0]) + 1]} (${int(max(pandlDiff))})")
print(f"Greatest Decrease in Profits: {date[int(minDateIndex[0]) + 1]} (${int(min(pandlDiff))})")

# Specify the file to write to
output_path = os.path.join("FinancialAnalysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------------------------\n")
    txtfile.write(f"Total Months: {len(date)}\n")
    txtfile.write(f"Total: ${int(sum(pandl))}\n")
    txtfile.write(f"Average Change: ${round(mean(pandlDiff),2)}\n")
    txtfile.write(f"Greatest Increase in Profits: {date[int(maxDateIndex[0]) + 1]} (${int(max(pandlDiff))})\n")
    txtfile.write(f"Greatest Decrease in Profits: {date[int(minDateIndex[0]) + 1]} (${int(min(pandlDiff))})\n")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    