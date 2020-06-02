import re

# Using grouping
phoneNumberPattern2 = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d)")
phoneNumber2 = phoneNumberPattern2.search(f"My number is 125-549-1274")

# Using the groups
print(phoneNumber2.group(0)) # The whole thing which was found
print(phoneNumber2.group(1)) # The first group in the parentheses
print(phoneNumber2.group(2)) # The second group in the parentheses
print(phoneNumber2.group(3)) # The third group in the parentheses
print(phoneNumber2.groups()) # All the different groups

# Setting different variables to the groups
g1, g2, g3 = phoneNumber2.groups()
# Printing them out
print(g1)
print(g2)
print(g3)
