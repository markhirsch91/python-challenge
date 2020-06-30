import os
import csv

# Path for the PyBank CSV file
py_poll_csv = os.path.join('py_poll.csv')
pypollOutput = open('pypolloutput.txt', 'w')


# Turning the columns from the CSV file into lists in order to properly make calculations.
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
    # Converting candidates to a set that will hold only unique values, the back to a list once again
    uniqueCandidates = list(set(candidates))

    
    print()
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes:  {totalVotesNumber}")
    print("-------------------------")
    
    
    for candidate in uniqueCandidates:
        print(f"{candidate}: {round((candidates.count(candidate)/totalVotesNumber)*100)}% ({candidates.count(candidate)})")
        
    print("-------------------------")
    print(f"Winner: {max(set(candidates), key=candidates.count)}")
    print("-------------------------")



# Exporting the Financial Analysis to pypolloutput.txt - located in analysis/pypolloutput.txt
pypollOutput.write("Election Results\n")
pypollOutput.write("-------------------------\n")
pypollOutput.write(f"Total Votes:  {totalVotesNumber}\n")
pypollOutput.write("-------------------------\n")
pypollOutput.write(f"{candidate}: {round((candidates.count(candidate)/totalVotesNumber)*100)}% ({candidates.count(candidate)})\n")
pypollOutput.write("-------------------------\n")
pypollOutput.write(f"Winner: {max(set(candidates), key=candidates.count)}\n")
pypollOutput.write("-------------------------\n")