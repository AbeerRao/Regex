import re

# The patterns
haPattern1 = re.compile(r'(ha){2}') # This pattern matches two instances of 'ha'. That is 'haha'
haPattern2 = re.compile(r'(ha){1,3}') # This pattern matches one to three instances of 'ha'
haPattern3 = re.compile(r'(ha){, 4}') # This pattern matches zero to four instances of 'ha
haPattern4 = re.compile(r'(ha){2, }') # This pattern matches two or more instances of 'ha'
nonGreedy1 = re.compile(r'(ha){3,5}?') # This pattern matches the shortest result of 'ha'
