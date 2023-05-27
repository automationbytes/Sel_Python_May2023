import re

transaction = "abc123af27052023"
#a = re.sub("[a-zA-Z]","",transaction) #only numbers
#a = re.sub("[0-9]","",transaction) #only alphabets
#a = re.sub("\D","",transaction) # only numbers
a = re.sub("\d","",transaction) # only alphabets


print(a)

transaction = "abc123af27052023"
t = re.findall("[a-zA-Z]",transaction)
print(t)

import re
pattern = r'\d{3}-\d{3}-\d{4}'
regex = re.compile(pattern)
phonenum = "Tom:123-456-7890,Tim:874-569-9105"

if regex.findall(phonenum):
    print("Match found",regex.findall(phonenum))
else:
    print("Not found")