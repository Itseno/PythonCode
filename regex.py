import re

whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
myStr = input("enter a sentence: ")
myStr = ''.join(filter(whitelist.__contains__, myStr))
print(myStr)
re.sub(' +',' ', myStr)
print(myStr)
