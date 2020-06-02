import re

# Using the pipe symbol '|'
heroPattern = re.compile(r'Iron Man | Thor')
# Assigning the variables
hero1 = heroPattern.search("I like Iron Man.")
hero2 = heroPattern.search("I like Thor.")
hero3 = heroPattern.search("I like Iron Man and Thor")
# Printing using the groups
print(hero3.group()) # Iron Man is printed out because it is the first word to match the
                     # pattern

# Making another pattern that can use other endings
batPattern = re.compile(r'Bat(man|mobile|woman|copter)')
# Searching the pattern
bat1 = batPattern.search('Batcopter is the best helicopter!')
bat2 = batPattern.search('Batmobile is a car or a bike?')
# Printing them out
print(bat1.group())
print(bat2.group())
