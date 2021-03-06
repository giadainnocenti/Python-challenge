# Python-challenge
Python scripts for analyzing financial records (**PyBank**) and poll data (**PyPoll**). \
The scripts can be found in the respective folders an they rely on the following python modules: **_os_** and **_csv_**.

## PyBank
The python script delevoped is found in the folder PyBank ([main.py](./PyBank/main.py)) is analyzing fairly simple financial records ([Pybank/Resources/budget_data.csv](Pybank/Resources/budget_data.csv)) of an hypothetical company. \
The python script is able to read the financial record dataset, which is composed by only two columns: *Date*, and *Profit/Losses*. The Profit/Losses are reported for each month. \
The script is analyzing the records and calculating:
* The total number of months
* The net total amount of Profit/Losses over the entire period, and the average of those changes
* The greatest increase and deacrease in profit for the entire period, showing both the date and the amount.\

The script is printing both on the screen and on a [text file](./PyBank/Output/financial_analysis.txt) the results of the financial analysis.



## PyPoll
The python script developed is in the folder PyPoll ([main.py](./PyPoll/main.py)). The aim of the code is to modernize the vote counting process of an hypotetical small, rural town. \
The set of Poll data is in a CSV file called [election_data.csv](Pypoll/Resources/Election_data.csv). The dataset is composed of three columns: *Voter ID*, *County* and *Candidate*.\
The script is reading the data and printing both on the screen and in a [text file](Pypoll/Output/Election_results.txt):
* The total number of votes received
* The name of each candidate along with the percentage of votes and the total number of votes received.
* The name of the winner.

## Copyright

Trilogy Education Services © 2019. All Rights Reserved.




