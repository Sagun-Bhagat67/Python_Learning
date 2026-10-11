# Write a program using functions to find greatest of three numbers. 

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

def great(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
print(f"The greatest of{a},{b},{c} is: {great(a,b,c)}")