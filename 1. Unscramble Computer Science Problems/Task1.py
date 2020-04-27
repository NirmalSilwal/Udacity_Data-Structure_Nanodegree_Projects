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


def count_phone_num(text, call):
    record_total = []

    for text_detail, call_detail in zip(text, call):
        record_total.extend([text_detail[0], text_detail[1], call_detail[0], call_detail[1]])

    return len(set(record_total))


total_records = count_phone_num(texts, calls)

print(f"There are {total_records} different telephone numbers in the records.")