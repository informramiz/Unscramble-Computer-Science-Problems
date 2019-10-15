"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
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

#a dictionary to hold call duration for each number
number_duration_dictionary = {}
for caller, receiver, _, duration in calls:
    #we need the duration in integer so that we can add
    intDuration = int(duration)
    #consider the caller duration on call
    number_duration_dictionary[caller] = number_duration_dictionary.get(caller, 0) + intDuration
    #as time spent on receiving a call is also considered so consider receiver as well
    number_duration_dictionary[receiver] = number_duration_dictionary.get(receiver, 0) + intDuration

max_duration = 0
number_with_max_duration = None
for number, duration in number_duration_dictionary.items():
    if max_duration < duration:
        max_duration = duration
        number_with_max_duration = number


print("%s spent the longest time, %d seconds, on the phone during September 2016." % (number_with_max_duration, max_duration))
