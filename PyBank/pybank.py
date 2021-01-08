import os
import csv

# Select the folder containing the CSV file
csvpath = os.path.join('.','Resources', 'budget_data.csv')

# creation of two lists to store the month-year as a string and the budget data as an integer.
period = []
budget_data = []
# open the CSV file in the specified directory.
with open(csvpath, 'r') as csvfile:
    #start reading the CSV file using a comma as delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    #skipping the header
    header = next(csvreader)
    
    # read every row in the file and append each row at the correct list
    for row in csvreader:
        period.append(row[0])
        budget_data.append(int(row[1]))
csvfile.close()

# setting up the name and the directory for the output file
financialanalysis = os.path.join(".", "Output", "financial_analysis.txt")

#opening the output file
analysis = open(financialanalysis, 'w') 
#print the headings on the terminal screen and the output file
print("```text \n Financial Analysis \n ----------------------------")
analysis.write("```text \n Financial Analysis \n ---------------------------- \n")

# Calculate the total number of months included in the dataset
months = len(period)
print(f"Total months: {months}")
analysis.write(f"Total months: {months} \n")
# Evaluate the net total amount of "Profit/Losses" over the entire period
net_total =  sum(budget_data)
print(f"Total: ${net_total}")
analysis.write(f"Total: ${net_total} \n")
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
change = []
for index in range(len(budget_data)-1):
    change.append(budget_data[index+1]-budget_data[index])
average_change = sum(change)/len(change)
print(f"Average  Change: ${average_change:8.2f}")
analysis.write(f"Average  Change: ${average_change:8.2f} \n")
# Evaluate the greatest increase in profits (date and amount) over the entire period
greatest_profit = max(budget_data)
print(f"Greatest Increase in Profits: {period[budget_data.index(greatest_profit)]} (${greatest_profit})")
analysis.write(f"Greatest Increase in Profits: {period[budget_data.index(greatest_profit)]} (${greatest_profit}) \n")
# Evaluate the greatest decrease in losses (date and amount) over the entire period
lowest_profit = min(budget_data)
print(f"Greatest Decrease in Profits: {period[budget_data.index(lowest_profit)]} (${lowest_profit})")
analysis.write(f"Greatest Decrease in Profits: {period[budget_data.index(lowest_profit)]} (${lowest_profit}) \n")
#close the output file
analysis.close()