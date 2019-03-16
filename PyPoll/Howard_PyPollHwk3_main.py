#UofMN Data Analytics Bootcamp
#Homework 3 PyPoll final solution
#Created by Chris Howard
#03/16/2019


import os
import csv
from operator import itemgetter

polls_csv = os.path.join("election_data.csv")

#extra function to count votes per voter ID number and list numbers with votes geater than 1
def FraudCheck():
    
    with open(polls_csv, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        csv_header = next(csvfile)
        voterDict = {}
        for row in csvreader:
            if row[0] in voterDict:
                voterDict[row[0]] = voterDict[row[0]] + 1
            else:
                voterDict[row[0]] = 1

    too_many = [key for key, value in voterDict.items() if value > 1]
    if len(too_many) != 0:
        print("The following voters voted multiple times:")
        for num in too_many:
            print(num)
    else:
        print("No voters voted more than once.")

#Give user a chance to check for voter fraud, can be skipped to just show results
voterFraud = input("Do you want to check for voter fraud [Yes]? ")
if voterFraud == "Yes":
    FraudCheck()

#Read votes as candidate names into a single list
with open(polls_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    votes = [row[2] for row in csvreader]

#list of unique candidates    
candidates = list(set(votes)) 
#list for candidate total votes
voteTotal = [] 
#list for candidate percentage of total votes
votePct = []

for candidate in candidates:
    voteTotal.append(votes.count(candidate))
    votePct.append(votes.count(candidate)/len(votes))

#zip lists together to give results for each candidate, then sort by highest vote total    
results = list(zip(candidates, voteTotal, votePct))
resultsSorted = sorted(results, key=itemgetter(1), reverse=True)

#Output formatted results to the console
print("Election Results")
print("-------------------")
print(f"Total Votes: {len(votes)}")
print("-------------------")
for result in resultsSorted:
    print(f"{result[0]}:     \t{round(result[2]*100, 3)}% ({result[1]})")
print("-------------------")
print(f"Winner: {resultsSorted[0][0]}")
print("-------------------")

#Output formatted results to a text file
output_path = os.path.join("ElectionResults.txt")

with open(output_path, 'w') as txtfile:

    txtfile.write("Election Results\n")
    txtfile.write("-------------------\n")
    txtfile.write(f"Total Votes: {len(votes)}\n")
    txtfile.write("-------------------\n")
    for result in resultsSorted:
        txtfile.write(f"{result[0]}:     \t{round(result[2]*100, 3)}% ({result[1]})\n")
    txtfile.write("-------------------\n")
    txtfile.write(f"Winner: {resultsSorted[0][0]}\n")
    txtfile.write("-------------------\n")
