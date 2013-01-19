# Filename: master_or_visa.py
# Author: Samantha Ai
# Index No: 10
# Description: Devise an algorithm to categorize if a user input credit card number belongs to MasterCard or VISA

# Ask for input number
cc_num = input("Enter credit card number without dashes: ")

# VISA - length 13/16, first digit 4
# MasterCard - length 16, first digit 5
if len(cc_num) == 13:
    cat = 'VISA'
elif len(cc_num) == 16:
    if cc_num[0] == '4':
        cat = 'VISA'
    elif cc_num[0] == '5':
        cat = 'MasterCard'
    else:
        cat = 'Not VISA or MasterCard'
else:
    cat = 'Not VISA or MasterCard'

print(cat)
