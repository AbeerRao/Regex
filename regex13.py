import re

# Making your own characters
atRegex = re.compile(r'.at') # The '.' means the pattern would match any word ending with 'at'. This matches only 2 characters to the left of the word

# Taking an input
sentence = input("Enter a sentence:  ")
# Using the findall for the vowel
sentenceFound = atRegex.findall(sentence)

# Printing the result
print(sentenceFound)
