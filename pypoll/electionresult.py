import os
import csv

csvpath = os.path.join('..','Data Analytics Bootcamp','election_data.csv')

count=0

candidates={"Charles Casper Stockham":0,"Diana DeGette":0,"Raymon Anthony Doane":0}

# Gathering candidates
with open(csvpath, 'r') as poll:
    reader = csv.reader(poll)
    next(reader)
    for row in reader:
        count=count+1
        if row[2]== "Charles Casper Stockham":
            candidates["Charles Casper Stockham"]+=1
        elif row[2]== "Diana DeGette":
            candidates["Diana DeGette"]+=1
        elif row[2]== "Raymon Anthony Doane":
            candidates["Raymon Anthony Doane"]+=1

#Gathering total votes cast
values = candidates.values()
totalvotes=sum(values)

ccs=candidates.get("Charles Casper Stockham")
dg=candidates.get("Diana DeGette")
rad=candidates.get("Raymon Anthony Doane")

#Percentage of total votes per candidate
percentccs = round(ccs/totalvotes * 100,3)
percentdg = round(dg/totalvotes * 100,3)
percentrad = round(rad/totalvotes * 100,3)

#Determining the winner
if percentccs > percentdg and percentrad:
    winner="Charles Casper Stockham"
elif percentdg > percentccs and percentrad:
    winner="Diana DeGette"
elif percentrad > percentccs and percentdg:
    winner="Raymon Anthony Doane"


print("Election Results")
print("---------------------")
print(f"Total Votes: {count}")
print("---------------------")
print(f"Charles Casper Stockham: {percentccs}% ({ccs})")
print(f"Diana DeGette: {percentdg}% ({dg})")
print(f"Raymon Anthony Doane: {percentrad}% ({rad})")
print(f"--------------------")
print(f"Winner: {winner}")
print(f"--------------------")

