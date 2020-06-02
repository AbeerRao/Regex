import re

# Making your own characters
vowelRegex = re.compile(r'[aeiouAEIOU]')

# Taking an input
sentence = input("Enter a sentence:  ")
# Using the findall for the vowel
sentenceFound = vowelRegex.findall(sentence)

# Printing the result
print(sentenceFound)
