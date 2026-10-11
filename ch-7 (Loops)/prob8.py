'''
Write a program to print the following star pattern: 
for n = 3 

* 
** 
***      
'''
n = int(input("Enter a number: "))
print(f"The required patttern for n = {n} is: \n")

for i in range(1,n+1):
    print("*"*i,end="")
    # print(" "*(n-i), end="") # No need for this line in  above pattern
    print("")
print("Done!!!!!!")