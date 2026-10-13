# 1. Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’. 

with open("poem.txt") as f:
    txt = f.read()
    if ('twinkle' in txt):
        print("Found the word Twinkle")
    else:
        print("Didn't folund the word")