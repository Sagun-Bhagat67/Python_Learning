#  Write a program to find the greatest of four numbers entered by the user. 

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))
d = int(input("Enter number d: "))

if(a>b and a>c and a>d):
     print(a,"Is greater")
elif(b>a and b>c and b>d):
    print(b,"Is Greater") 
elif(c>a and c>b and c>d):
    print(c,"is Greater")   
else:
    print(d,"is Greater")
    