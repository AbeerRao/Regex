import re

# Making your own characters
nameRegex = re.compile(r'Name : (.*)') # The star matches any word. Use '?' for nongreedy

# Taking an input
sentence = input("Enter your name:  ")
# Using the findall for the vowel
sentenceFound = nameRegex.findall(sentence)

# Printing the result
print(sentenceFound)
