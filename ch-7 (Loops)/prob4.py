#  Write a program to find whether a given number is prime or not.
n = int(input("Enter a number to checki prime or not : "))

flag = 0
for i in range(1,n):
    if(n%i==0):
        flag = flag+1
    
if(flag == 1):
    print("The number is prime.")
else:
    print("The number is composite.")