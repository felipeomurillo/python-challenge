# ---------------------------------------------------------------
# Name: main.py
# Created by: Felipe Murillo
# Date Created: April 2, 2020
#
# Description: Inputs data from ../Resources/election_data.csv 
# to output an Election Results summary
#
# Inputs: 
# election_data.csv > Vote for candidate by Voter ID and voter county
#
# Outputs:
# Screen and ./Analysis/election_results.txt 
# ---------------------------------------------------------------

# Import modules to manipulate filesystems
import os
import csv

# Specify path to input data
csvpath = os.path.join("..","Resources","election_data.csv")

# Open input data file
with open(csvpath) as csvfile:

    # Read file as comma delimited
    csvreader = csv.reader(csvfile,delimiter = ',')

    # Skip data contained in header (i.e., 1st row)
    next(csvreader)

    # Initialize working lists
    no_votes = 0
    summary_data = []
    candidate_names = []
    vote_count = []

    for row in csvreader:
        # Count the number of total votes in data set
        no_votes += 1
        # Gather all unique candidates and initialize their vote count to 0
        if row[2] not in candidate_names:  # Gather all possible candidates names 
            candidate_names.append(row[2])
            vote_count.append(0)
        # Count votes received by each candidate
        for name in candidate_names:
            if name == row[2]:
                vote_count[candidate_names.index(name)] += 1
            
# Calculate Voter Percentages
percentage = [votes/no_votes*100 for votes in vote_count]

# Determine Winner
winner = candidate_names[vote_count.index(max(vote_count))]

# Compile Summary Results
summary_data.append("Election Results            ")
summary_data.append("----------------------------")
summary_data.append(f"Total Votes: {no_votes}")
summary_data.append("----------------------------")
for name in candidate_names:
    i = candidate_names.index(name)
    summary_data.append(f'{name}: {percentage[i]:.3f}% ({vote_count[i]})')
summary_data.append("----------------------------")
summary_data.append(f"Winner: {winner}")
summary_data.append("----------------------------")

# Print summary to screen
for i in summary_data:
    print(i)

# Save a copy of the election results to ../Analysis/election_results.txt
output =  os.path.join("..","Analysis","election_results.txt")

# If the Output folder does not exist, create it; if it does, use it!
os.makedirs(os.path.dirname(output), exist_ok=True)

# Write output to txt file and close it when done
with open(output,"w") as txtfile:
    for j in summary_data:
        txtfile.write(j)
        txtfile.write("\n")
    txtfile.close()