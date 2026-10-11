'''
Write a program to print the following star pattern. 
for n = 3 
* * * 
*   *    
* * *  
'''
n = int(input("Enter a number: "))
print(f"Pattern for n = {n} is : \n")

for i in range(1,n+1):
    if(i == 1):
        print("*"*n)
    elif(i == n):
        print("*"*n)
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
        print("")
print("Done!!!!!!")