import os
import csv

# Path to the PyBank CSV file
py_bank_csv = os.path.join('py_bank.csv')


#Printing out the title and seperation line
print()
print()
print("Financial Analysis")
print("----------------------------")

#Turning the colums from the CSV file  into lists in order to properly make calculations. They will be placed inside of these lists:
months = []
monthlyChange = []
profitLosses = []

with open(py_bank_csv) as csvfile:
    # Splits data between commas
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)


# Finding the number of Months and the total "Profits/Losses" column
    for row in csvreader:
        months.append(row[0])
        profitLosses.append(int(row[1]))
        totalMonths = len(months)
        totalProfitLosses = sum(profitLosses)
        #monthlychange = sum(profitLosses) / months

# Setting up monthly change
    for x in range(len(profitLosses)-1):
        monthlyChange.append(profitLosses[x+1] - profitLosses[x])
        averageMonthlyChange = (sum(monthlyChange)/len(monthlyChange))
        maxMonthlyChange = max(monthlyChange)
        minMonthlyChange = min(monthlyChange)
        
        




#Printing the calculations from above ^^

print(f"Total Months:  {totalMonths}")
print(f"Total: ${totalProfitLosses}")
print(f"Average Change: $ {averageMonthlyChange}")
print(f"Greatest Increase in Profits: (${maxMonthlyChange}) ")
print(f"Greatest Decrease in Profits: (${minMonthlyChange}) ")








    




    








    


