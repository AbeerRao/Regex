import re

# Making a pattern
noNewLineRegex = re.compile(r'.*') # '.*' matches everything but newline. If you add 're.DOTALL', everything would be matched

# Searching for it
answer = noNewLineRegex.search("Hello everyone!\nMy name is Abeer Rao.\nBye!").group()
# Printing it out
print(answer)
