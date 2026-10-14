#  Repeat program 3 for a list of such words to be censored. 

'''
A file contains a word “Donkey” multiple times. You need to write a program 
which replace this word with ##### by updating the same file. 
'''
words = ['donkey','gadhe','bhadwa','fuck','chutiya','bitch']
with open("donkey.txt") as f:
    content = f.read()
    content = content.lower()
    
for word in words:
    content = content.replace(word,"####")

with open("donkey.txt",'w') as f:
    f.write(content)
    