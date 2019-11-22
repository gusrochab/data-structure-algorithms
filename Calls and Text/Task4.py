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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

make_calls = []
receive_calls = []
make_text = []
receive_text = []
marketing = []

for register in calls:
    make_calls.append(register[0])
    receive_calls.append(register[1])

for register in texts:
    make_text.append(register[0])
    receive_text.append(register[1])

make_calls = set(make_calls)
receive_calls = set(receive_calls)
make_text = set(make_text)
receive_text = set(receive_text)

for num in make_calls:
    if num not in receive_calls:
        if num not in make_text:
            if num not in receive_text:
                marketing.append(num)

marketing.sort()
print("These numbers could be telemarketers: ")
for num in marketing:
    print(num)


#This algorthim is a O(nˆ2)