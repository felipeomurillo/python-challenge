# ---------------------------------------------------------------
# Name: main.py
# Created by: Felipe Murillo
# Date Created: April 1, 2020
#
# Description: Inputs data from ../Resources/budget_data.csv 
# to output a Financial Analysis summary
#
# Inputs: 
# budget_data.csv > monthly recording of profits/losses
#
# Outputs:
# Screen and ./Analysis/financial_summary.txt 
# ---------------------------------------------------------------

# Import modules to manipulate filesystems
import os
import csv

# Import average function from statistics module
from statistics import mean

# Specify path to input data
csvpath = os.path.join("..","Resources","budget_data.csv")

# Open input data file
with open(csvpath) as csvfile:

    # Read file as comma delimited
    csvreader = csv.reader(csvfile,delimiter = ',')

    # Skip data contained in header (i.e., 1st row)
    next(csvreader)

    # Initialize working lists
    months = []
    month_net = []
    deltas = []
    summary_data = []

    for row in csvreader:
        months.append(str(row[0]))       # Create months list
        month_net.append(int(row[1]))    # Create net profit/loss list

# Create list of delta changes between adjacent entries
for x in range(0,len(months)-1):
    deltas.append(month_net[x+1] - month_net[x])

# Find location of MAX and MIN delta change
max_index = deltas.index(max(deltas))
min_index = deltas.index(min(deltas))

# Collect and format desired entries for summary
summary_data.append("Financial Analysis         ")
summary_data.append("----------------------------")
summary_data.append(f"Total Months: {len(months)}")
summary_data.append(f"Total: ${sum(month_net[:])}")
summary_data.append(f"Average Change: ${mean(deltas[:]):.2f}")
summary_data.append(f"Greatest Increase in Profits: {months[max_index+1]} (${deltas[max_index]})")
summary_data.append(f"Greatest Increase in Profits: {months[min_index+1]} (${deltas[min_index]})")

# Print summary to screen
for i in summary_data:
    print(i)

# Save a copy of the financial summary to ../Analysis/financial_summary.txt
output =  os.path.join("..","Analysis","financial_summary.txt")

# If the Output folder does not exist, create it; if it does, use it!
os.makedirs(os.path.dirname(output), exist_ok=True)

# Write output to txt file and close it when done
with open(output,"w") as txtfile:
    for j in summary_data:
        txtfile.write(j)
        txtfile.write("\n")
    txtfile.close()