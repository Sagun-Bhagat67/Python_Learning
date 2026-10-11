# Write a program to find whether a given username contains less than 10 
# characters or not. 

name = input("Enter username: ")

if(len(name)>10):
    print(name,"is not a valid name\n It contain more than 10 characters")
else:
    print(name,"is a valid name\nIt contain less than 10 characters")
    