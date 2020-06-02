import re

# Making your own characters
notVowelRegex = re.compile(r'[^aeiouAEIOU]')

# Taking an input
sentence = input("Enter a sentence:  ")
# Using the findall for the vowel
sentenceFound = notVowelRegex.findall(sentence)

# Printing the result
print(sentenceFound)
