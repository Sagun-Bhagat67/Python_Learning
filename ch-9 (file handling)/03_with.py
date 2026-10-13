#To open a file we write

f=open("my_file.txt")
print(f.read())
f.close()

#The same this can be done by using with function
#Here you don't need to close the opened file 
#The syntax goes like this:

with open("my_file.txt") as f:
    print(f.read())
    
#You don't need to close the file 
    