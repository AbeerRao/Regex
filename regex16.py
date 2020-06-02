import re

# Making a pattern
namesRegex1 = re.compile(r'Agent \w+') # This matches 'Agent' and any word after it
namesRegex2 = re.compile(r'Agent (\w)\w*')

# Substituting the values
secretNames1 = namesRegex1.sub("CENSORED", "Agent Abeer gave the secret key to Agent Addu")
secretNames2 = namesRegex2.sub(r'\1****', "Agent Dogla gave the secret key to Agent Doggy")
# Printing the answer
print(secretNames1) # 'Agent Abeer' and 'Agent Addu' get replaced with 'CENSORED'
print(secretNames2) # 'Agent Dogla' and 'Agent Doggy' get replaced with 'D****'
