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

#A helper function to count numbers for each type of recod
def count_distinct_numbers_each(records, dictionary = {}):
    distinct_numbers_count = 0
    for record in records:
        #first 2 recorders of either calls or texts are numbers so check each
        for number in list(record[0:2]):
            #only count a number if it does not exist already in the dictionary
            if number not in dictionary:
                distinct_numbers_count += 1
                dictionary[number] = True
    return distinct_numbers_count

# write a function that count the distinct numbers, to avoid code duplication
def count_distinct_numbers(calls, texts):
    #a dictionary to mark numbers as counted
    dictionary = {}
    #count distinct numbers in calls
    distinct_numbers_count = count_distinct_numbers_each(calls, dictionary)
    #count distinct numbers in texts records
    distinct_numbers_count += count_distinct_numbers_each(texts, dictionary)
    return distinct_numbers_count

distinct_numbers_count = count_distinct_numbers(calls, texts)
print("There are %s different telephone numbers in the records." % distinct_numbers_count)
