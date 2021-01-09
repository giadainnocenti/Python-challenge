import os
import csv

#defining a function to print the delimiter string
def delimiter(filename, string):
    print(string)
    filename.write(string)
    filename.write('\n')
    return()
def divider():
    return ("-------------------------")

csvpath = os.path.join('.','Resources','election_data.csv')

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    voter_ID = []
    county = []
    candidates = []
    for row in csvreader:
        voter_ID.append(row[0])
        county.append(row[1])
        candidates.append(row[2])
csvfile.close()

resultpath = os.path.join('.','Output','Election_results.txt')

result = open(resultpath, 'w')
string ="*** Text \nElection Results "
delimiter(result, string)
delimiter(result, divider())


#The total number of votes cast
total_votes = len(candidates)
string = f"Total Votes: {total_votes}"
delimiter(result, string)
delimiter(result, divider())
# A complete list of candidates who received votes
candidate_list = []
for candidate in candidates:
    if candidate not in candidate_list:
        candidate_list.append(candidate)

winner_votes = 0
for candidate in candidate_list:
# The total number of votes each candidate won
    candidate_votes = candidates.count(candidate)
# The percentage of votes each candidate won
    percentage = candidate_votes/total_votes
    string = f"{candidate}: {percentage:0.3%} ({candidate_votes})"
    delimiter(result, string)
    
# The winner of the election based on popular vote.
    if candidate_votes > winner_votes:
        winner_votes = candidate_votes
        winner = candidate
    elif candidate_votes == winner_votes:
        string = f'WARNING: {winner} and {candidate} have the same number of votes'
        delimiter(result, string)

delimiter(result, divider())
string = f"Winner: {winner}"
delimiter(result, string)
delimiter(result, divider())
string = f"***"
delimiter(result, string)
#close the output file
result.close()

