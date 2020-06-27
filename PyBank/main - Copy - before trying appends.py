import os
import csv

# Path for the PyBank CSV file
py_bank_csv = os.path.join('py_bank.csv')


months =[]
monthlyChange = []
totalProfit =[]

with open(py_bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        months.append(row[0])
        totalProfit.append(int(row[1]))

#Counting the rows
    # monthData = list(csvreader)
    # rowcount = len(monthData)
    #rowcount = sum(1 for row in csvreader)

    # Calculating the net total amount of "Profit/Losses"
    money = 0
    profitSum = 0
    lossSum = 0
    totalProfitLosses = 0
    
    for row in csvreader:
        money = int(row[1])
        if money > 0:
            profitSum += money
        elif money < 0:
            lossSum += money

    totalProfitLosses = profitSum + lossSum


#Finding Monthly Change
    # monthlyChange= 0
    # for row in csvreader:
    #     monthlyChange = totalProfitLosses[row+1] - totalProfitLosses[row-1]



print()
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {len(months)}")
print(f"Total: ${sum(totalProfit)}")
#print(f"Monthly Change:  {monthlyChange}")


    




    








    
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

