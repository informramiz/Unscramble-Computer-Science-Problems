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
#numbers that received calls
call_receivers = set([r for _, r, _, _ in calls])
#numbers that either sent or received a text
texters = set([s for s, _, _ in texts])
#merge text senders with receivers as we only need number we are interested in either
texters.union(set([r for _, r, _ in texts]))

outgoing_only_numbers = set()
#for all the numbers that made calls but are not in call receiver, text sender or text receiver
#are the possible telemarketers
for number, _, _, _ in calls:
    if number not in call_receivers and number not in texters:
        outgoing_only_numbers.add(number)


telemarketers = sorted(outgoing_only_numbers)
print("These numbers could be telemarketers: ")
for number in telemarketers:
    print(number)
