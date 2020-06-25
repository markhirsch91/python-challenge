import os
import csv

# # Path for the PyBank CSV file
csvpath = os.path.join('py_bank.csv')



# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))




with open(csvpath) as csvfile:

    title = "Financial Analysis"
    print(title)
    seperator = "----------------------------"
    print(seperator)


    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #print(csvreader)

# Counting the rows
    data = list(csvreader)
    rowcount = len(data)
    totalMonthsLabel = 'Total Months: '
    print(totalMonthsLabel + str(rowcount))
    




    # # THIS DISPLAY EVERYTHING Read the header row first (skip this step if there is now header)
    # csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # # Read each row of data after the header
    # for row in csvreader:
    #     print(row)



    # dates = []
    # profits = []
    # for column in csvreader:
        
    #     date = column[0]
    #     profit = column[2]

    #     dates.append(date)
    #     profits.append(color)

    # print(dates)
    # print(profits)


