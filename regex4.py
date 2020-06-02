import re

# The pattern using '?' which makes it optional
fullNamePattern = re.compile(r'Dan(iel)? Collins') # 'iel' is optional. The name can be 'Dan Collins' or 'Daniel Collins'
# Getting the name
nameInput = input('What is your name?  ')
# Searching
nameSearch = fullNamePattern.search(nameInput)
# Seeing if there is a name
if nameSearch == None:
    print(f"No name found")
else:
    print(f"Name found: {nameSearch.group()}")
