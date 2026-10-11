# Recursion basicaslly mean a block of code(called function) calls itself until base condition is meet 
#Best example for recursionj is factorial 
'''
fact(1) =  1
fact(2) =  2 x 1
fact(3) =  3 x 2 x 1
fact(4) =  4 x 3 x 2 x 1
fact(5) =  5 x 4 x 3 x 2 x 1

fact(n) = n x n-1 x n-2 x..........x 3 x 2 x 1

fact(n) = n x fact(n-1)
'''

def fact(n):
    if(n ==0 or n ==1 ):
        return 1
    else:
        return n* fact(n-1)
    
n = int(input("Enter a number: "))
print(f"The factorial of {n} is: {fact(n)}")