"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
from datetime import datetime
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

time = int(calls[0][3])
i = 0
for register in calls:
    if int(register[3]) > time:
        time = int(register[3])
        number = register[0]

print('{} spent the longest time, {} seconds, on the phone during September 2016'.format(number, time))

#This algorithm is a O(n)

