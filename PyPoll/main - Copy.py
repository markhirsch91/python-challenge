import os
import csv

# Path for the PyBank CSV file
py_poll_csv = os.path.join('py_poll.csv')


#Empty Lists
voterID =[]
candidates = []
totalVotesCount= []
ontooleyChangeList = []

with open(py_poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

# Assigning my new empty list from above "totalVotesCount" to the first column in the CSV
# since each voter ID is unique.
    for row in csvreader:
        totalVotesCount.append(row[0])
        totalVotesNumber = len(totalVotesCount)
        candidates.append(str(row[2]))
        


print()
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {totalVotesNumber}")
print("-------------------------")



print(f"Khan: {round((candidates.count('Khan')/totalVotesNumber)*100)}% ({candidates.count('Khan')})")
print(f"Correy: {round((candidates.count('Correy')/totalVotesNumber)*100)}% ({candidates.count('Correy')})")
print(f"Li: {round((candidates.count('Li')/totalVotesNumber)*100)}% ({candidates.count('Li')})")
#print(f"O'Tooley: {round((candidates.count('O\'Tooley')/totalVotesNumber)*100)}% ({candidates.count('O\'Tooley')})")
print("-------------------------")
print("Winner: ")
print("-------------------------")




