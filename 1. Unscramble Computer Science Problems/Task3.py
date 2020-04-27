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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


# part 1 solution

def find_unique_codes(bangalore_callers):
    codes = []

    for users in bangalore_callers:

        receiver = users[1]

        if receiver[:2] == '(0':
            codes.append(receiver[1:4])

        if receiver[:3] == '140':
            codes.append('140')

        if receiver[0] == '7' or receiver[0] == '8' or receiver[0] == '9':
            codes.append(receiver[:4])

    unique_code = sorted(list(set(codes)))

    return unique_code


# part 2 solution

def percentage_receiver(bangalore_callers):
    bangalore_receiver = [user[1] for user in bangalore_callers if user[1][:5] == '(080)']

    percentage = len(bangalore_receiver) / len(bangalore_callers) * 100

    return percentage


bangalore_caller = [[details[0], details[1]] for details in calls if details[0][:5] == '(080)']

unique_codes = find_unique_codes(bangalore_caller)

print("The numbers called by people in Bangalore have codes:")
for ph_code in unique_codes:
    print(ph_code)

percentages = percentage_receiver(bangalore_caller)
print("\n{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
    percentages))