import os
import csv




# Path for the PyBank CSV file
py_poll_csv = os.path.join('py_poll.csv')


#Empty Lists
voterID =[]
candidates = []
totalVotesCount= []
ontooleyChangeList = []
#name = "O'Tooley"

with open(py_poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

# Assigning my new empty list from above "totalVotesCount" to the first column in the CSV
# since each voter ID is unique.
    for row in csvreader:
        totalVotesCount.append(row[0])
        totalVotesNumber = len(totalVotesCount)
        candidates.append(str(row[2]))    
    # your current list of candidates can be converted to a set which only hold unique values, then back to a list to make it easier to work with
    uniqueCandidates = list(set(candidates))
    # using this, you can loop through the data and print results like so
    
    print()
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes:  {totalVotesNumber}")
    print("-------------------------")
    
    
    for candidate in uniqueCandidates:
        print(f"{candidate}: {round((candidates.count(candidate)/totalVotesNumber)*100)}% ({candidates.count(candidate)})")
        
    print("-------------------------")
    #print(f"Winner: {max(int(candidates.count(candidate))} ")
    print(f"Winner: {max(set(candidates), key=candidates.count)}")
    print("-------------------------")    






