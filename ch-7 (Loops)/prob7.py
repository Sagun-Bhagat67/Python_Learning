'''
Write a program to print the following star pattern. 
for n = 3 
  * 
 *** 
***** 
'''
n = int(input("Enter no. of row of stars: "))

print(f"The star pattern for n = {n} is: \n")
for i in range(1,n+1):
    print(" "*(n-i), end="") #prints space with no new line (by the help of end="" statement)
    print("*"*(2*i-1), end="") #prints stars with no new line 
    print("") # Adds new line
    