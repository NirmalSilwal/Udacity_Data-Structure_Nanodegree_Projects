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


def find_telephone_duration(call):
    person_list = {}

    for details in call:

        if details[0] not in person_list.keys():

            person_list[details[0]] = details[-1]

        else:
            person_list.update({details[0]: int(person_list[details[0]]) + int(details[-1])})

        if details[1] not in person_list.keys():

            person_list[details[1]] = details[-1]

        else:
            person_list.update({details[1]: int(person_list[details[1]]) + int(details[-1])})

    all_call_durations = [int(i) for i in person_list.values()] 
    max_duration = max(all_call_durations)

    for k in person_list.keys():
        if person_list[k] == max_duration:
            telephone = k
            break

    return telephone, max_duration


phone, longest_duration = find_telephone_duration(calls)

print(f"{phone} spent the longest time, {longest_duration} seconds, on the phone during September 2016.")



