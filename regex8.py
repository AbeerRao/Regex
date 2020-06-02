import re

# Creating a pattern
phoneNumberPattern = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
# Finding the pattern
print(phoneNumberPattern.findall('123-456-7890 is the number for a particular person.'))
