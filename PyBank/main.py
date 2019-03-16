#UofMN Data Analytics Bootcamp
#Homework 3 PyBank final solution
#Created by Chris Howard
#03/16/2019


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
    

    # Read through each row of data after the header
    for row in csvreader:
        #print(row)
        date.append(row[0])
        pandl.append(float(row[1]))

#find differences from one month to the next and save to array
pandlDiff = np.diff(pandl)

#find index of greatest increase and decrease month over month
maxDateIndex = np.where(pandlDiff == max(pandlDiff))
minDateIndex = np.where(pandlDiff == min(pandlDiff))

print("Financial Analysis")
print("---------------------------------")
print(f"Total Months: {len(date)}") #total number of months = length of date list
print(f"Total: ${int(sum(pandl))}") #total P&L over all months
print(f"Average Change: ${round(mean(pandlDiff),2)}") #average of differential list
print(f"Greatest Increase in Profits: {date[int(maxDateIndex[0]) + 1]} (${int(max(pandlDiff))})") #date index associated with max increase 
print(f"Greatest Decrease in Profits: {date[int(minDateIndex[0]) + 1]} (${int(min(pandlDiff))})") #date index associated with max decrease

# Write console output to .txt file (better formatting than csv)
output_path = os.path.join("FinancialAnalysis.txt")

with open(output_path, 'w') as txtfile:

    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------------------------\n")
    txtfile.write(f"Total Months: {len(date)}\n")
    txtfile.write(f"Total: ${int(sum(pandl))}\n")
    txtfile.write(f"Average Change: ${round(mean(pandlDiff),2)}\n")
    txtfile.write(f"Greatest Increase in Profits: {date[int(maxDateIndex[0]) + 1]} (${int(max(pandlDiff))})\n")
    txtfile.write(f"Greatest Decrease in Profits: {date[int(minDateIndex[0]) + 1]} (${int(min(pandlDiff))})\n")
 