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

# Finding the number of months by counting the rows
    data = list(csvreader)
    rowcount = len(data)
    print(f"Total Months:  {rowcount}")

    # csv_reader = csv.reader(csv_file, delimiter=',')
    for lines in csvreader:
        print(f"Profits: {lines[0]}")


    
#Finding the net total amount of "Profits/Losses" by     
    # totalProfitLosses = sum(row[1]for row in csvreader)
    

    # Define the function and have it accept the 'wrestler_data' as its sole parameter
    # def print_total(bank_data):
    # For readability, it can help to assign your values to variables with descriptive names
    #     profitLosses = sum(bank_data[1])

    # print(f"Total: {profitLosses}")
    #print(profit)


    # profitValues = (float(row[1])for row in csvreader)
    # totalProftLosses = sum(profitValues)
    # print(totalProfitLosses)


    




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


