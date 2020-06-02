import re

# Will use '*' for zero or more matching characters
pattern = re.compile(r'Bat(man)*boy') # The 'man' can be entered multiple times and it would still match. It can also be excluded.
# Getting the input from the user
input = input("Enter Batmanboy: ")
# Searching for the 'wow'
inputSearch = pattern.search(input)
# Seeing if there is a match
if inputSearch == None:
    print("Nothing found")
else:
    print(inputSearch.group())
