# Write a python function to remove a given word from a list and strip it at the same time 

l = ['Sagun','Gun','random','universe','unicorn','united','rameshwor']

def rm(l,word):
    nl = []
    for item in l:  
        if not(item == word):
            nl.append(item.strip(word))
    return nl

word = input("stripped word  = ")

print(l)
print(f"After strp and remove: {rm(l,word)}")