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


def possible_telemarketers(call, text):
    call_sender = list(set([details[0] for details in call]))
    call_receiver = list(set([details[1] for details in call]))
    text_sender = list(set([details[0] for details in text]))
    text_receiver = list(set([details[1] for details in text]))

    telemarketers = []

    for marketer in call_sender:
        if marketer not in call_receiver and marketer not in text_sender and marketer not in text_receiver:
            telemarketers.append(marketer)

    return sorted(telemarketers)


marketers = possible_telemarketers(calls, texts)

print("These numbers could be telemarketers: ")
for ph_num in marketers:
    print(ph_num)