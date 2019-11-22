"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
numbers = []
for register in texts:
    numbers.append(register[0])
    numbers.append(register[1])

for register in calls:
    numbers.append(register[0])
    numbers.append(register[1])

set_of_numbers = set(numbers)

print('There are {} different telephone numbers in the records'.format(len(set_of_numbers)))

#This algorithm is O(n)
