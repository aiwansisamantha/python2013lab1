# Filename: validate_mastervisa.py
# Author: Samantha Ai
# Index No: 10
# Description: Validate a user input MasterCard or VISA credit card number

# Ask for input number
cc_num = input("Enter credit card number without dashes: ")

# Both VISA and MasterCard use Luhn algorithm, so no need to differentiate

# Define check digit
check = int(cc_num[-1])

## 1.Counting from the check digit, which is the rightmost, and moving left, double the value of every second digit.
## 2.Sum the digits of the products (e.g., 10: 1 + 0 = 1, 14: 1 + 4 = 5) together with the undoubled digits from the original number.

if len(cc_num) == 13:
    n = 1
else:
    n = 0
total = 0
for num in range(0, len(cc_num)-1):
    n = n + 1
    digit = cc_num[num]
    if n % 2 == 0:
        # Double the digit
        digit = int(digit) * 2
        # Add individual digits together if doubled digit >= 10
        if digit >= 10:
            digit = str(digit)
            digit = int(digit[0]) + int(digit[1])
        total = total + digit
    else:
        total = total + int(digit)

 
## 3.If the total modulo 10 is equal to 0 (if the total ends in zero) then the number is valid according to the Luhn formula; else it is not valid.

## The check digit (x) is obtained by computing the sum of digits then computing 9 times that value modulo 10 (in equation form, (67 * 9 mod 10)). Eg:
## 1.Compute the sum of the digits (67).
## 2.Multiply by 9 (603).
## 3.The last digit, 3, is the check digit.

total = total * 9
total = str(total)
last = int(total[-1])
if last == check:
    valid = 'Valid number.'
else:
    valid = 'Invalid number.'

print(valid)
