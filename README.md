# Python-challenge
Python scripts for analyzing financial records (**PyBank**) and poll data (**PyPoll**). \n
The scripts can be found in the respective folders an it is relying only on the following python modules: **_os_** and **_csv_**

## PyBank
The python script delevoped is found in the folder PyBank ([main.py](./PyBank/main.py)) is analyzing fairly simple financial records ([Pybank/Resources/budget_data.csv](Pybank/Resources/budget_data.csv)) of an hypothetical company. \
The python script is able to read the financial record dataset, which is composed by only two columns: *Date*, and *Profit/Losses*. The profit losses are reported for each month. /
The script is analyzing the record and calculating:
* The total number of months
* The net total amount of Profit/Losses over the entire period, and the average of those changes
* The greatest increase and deacrease in profit for the entire period, showing both the date and the amount
/
The script is printing both on the screen and on a [text file](./PyBank/Output/financial_analysis.txt) the results of the financial analysis.



## PyPoll
The python script developed is in the folder PyPoll ([main.py](./PyPoll/main.py)). The aim of the code is to modernize the vote counting process of a small, rural town. /
The set of Poll data is in a CSV file called [election_data.csv](Pypoll/Resources/Election_data.csv). The dataset is composed of three columns: *Voter ID*, *County* and *Candidate*./




