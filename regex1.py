# Importing Regular expressions
import re

# Creating a pattern
phoneNumberPattern = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

# Taking an input from the user to be used in the
number = input("What is your phone number?")
# Finding the pattern
phoneNumber = phoneNumberPattern.search(f"My number is {number}")
# Printing the result
if phoneNumber == None:
    print("No number found")
else:
    print(f"Phone number found: {phoneNumber.group()}")
