# Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique.
dict = {}

for i in range(4):
    name = input("Enter name: ")
    lan = input("Enter Language: ")
    dict.update({name:lan})
    
print(dict)

for item in dict:
    print(item)
    
# If the names of 2 friends are same; what will happen to the program
dict.update({input("Enter name: "):input("Enter language: ")})

print(dict)