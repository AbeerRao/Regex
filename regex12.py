import re

# Making your own characters
helloRegex = re.compile(r'Hello$') # The '$' means the pattern should occur at only the end of the string

# Taking an input
sentence = input("Enter a sentence:  ")
# Using the findall for the vowel
sentenceFound = helloRegex.findall(sentence)

# Printing the result
print(sentenceFound)
