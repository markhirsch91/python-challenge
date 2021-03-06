import os
import csv

# Path to the PyBank CSV file
py_bank_csv = os.path.join('Resources','py_bank.csv')
py_bank_txt = os.path.join('analysis','pybankoutput.txt')
pybankOutput = open(py_bank_txt, 'w')

#Printing out the title and seperation line. Top two print() commands are there just for a cleaner look in the terminal
print()
print()
print("Financial Analysis")
print("----------------------------")



# totalMonths = 0

# Opening the CSV file from the path definied above. Splitting the  data between commas.
# csv_header allows me to not include the header row in the CSV file in my calculations

with open(py_bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Turning the columns from the CSV file into lists in order to properly make calculations.
    # dates stores the first column fro mthe CSV file.
    # monthlyChange finds the changes between each of the dats (or months in this case) and is used in the "for x" loop below
    # profitLosses is the second column in the CSV - "Profits/Losses
    dates = []
    monthlyChange = []
    profitLosses = []

# Finding the number of Months listed on the CSV file (using the [dates] list) and finding the Net Profit (or "Total") in the [profitLosses] list
    for row in csvreader:
        # dates will be the first column in the CSV (including the "Date-Year" values)
        dates.append(row[0])
        # Finding the Count of each entry in dates, and calling it "totalMonths"
        totalMonths = len(dates)
        # the amount of $ earned each month (column 2 in the CSV) is assigned to the profitLosses list
        profitLosses.append(int(row[1]))
        # the Net Profit is called "totalProfitLosses" in this case, use the sum() function to find the net protif of the total monthly revenue
        totalProfitLosses = sum(profitLosses)
        

# Finding the average change between each date/month. Each line is a new change, so I will use the profitLosses list. using "range" allows me to refer to lines before and after
    for x in range(len(profitLosses)-1):
        monthlyChange.append(profitLosses[x+1] - profitLosses[x])
        averageMonthlyChange = (sum(monthlyChange)/len(monthlyChange))
        # Rounding the averageMonthlyChange value to 2 decimal places
        roundedAverageMonthlyChange = round(averageMonthlyChange,2)
        # Finding the Greatest Increase in Profits and the month where that occured
        maxMonthlyChange = max(monthlyChange)
        maxMonthlyChangeValue = monthlyChange.index(maxMonthlyChange)
        # We're find the NEXT month (where the change is actually displayed in the list). To do list, "maxMonthlyChange+1" is used
        maxMonthlyChangeLabel = dates[maxMonthlyChangeValue+1]
        # Finding the Greatest Increase in Profits and the month where that occured
        minMonthlyChange = min(monthlyChange)
        minMonthlyChangeValue = monthlyChange.index(minMonthlyChange)
        # I'm finding the NEXT month (where the change is actually displayed in the list). To do list, "minMonthlyChange+1" is used
        minMonthlyChangeLabel = dates[minMonthlyChangeValue+1]
        

# Printing the variables found above with proper labels
print(f"Total Months:  {totalMonths}")
print(f"Total: ${totalProfitLosses}")
print(f"Average Change: ${roundedAverageMonthlyChange}")
print(f"Greatest Increase in Profits: {maxMonthlyChangeLabel} (${maxMonthlyChange}) ")
print(f"Greatest Decrease in Profits: {minMonthlyChangeLabel} (${minMonthlyChange}) ")



# Exporting the Financial Analysis to pybankoutput.txt - located in analysis/pybankoutput.txt
pybankOutput.write("Financial Analysis\n")
pybankOutput.write("----------------------------\n")
pybankOutput.write(f"Total Months:  {totalMonths}\n")
pybankOutput.write(f"Total: ${totalProfitLosses}\n")
pybankOutput.write(f"Average Change: $ {roundedAverageMonthlyChange}\n")
pybankOutput.write(f"Greatest Increase in Profits: {maxMonthlyChangeLabel} (${maxMonthlyChange})\n")
pybankOutput.write(f"Greatest Decrease in Profits: {minMonthlyChangeLabel} (${minMonthlyChange})\n")


pybankOutput.close()