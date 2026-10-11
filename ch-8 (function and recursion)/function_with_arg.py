#Function with argument and returning value

#function defination

def greet(name,roll):
    print(f"Hello {name}, Your roll no is: {roll}")
    return "okay sir"

name = input("Enter your name: ")
roll = input(f"Enter roll no of {name}: ")

#function call
a = greet(name,roll)
print(a)