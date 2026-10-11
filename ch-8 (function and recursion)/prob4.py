# Write a recursive function to calculate the sum of first n natural numbers.

n = int(input("Enter number n: "))

def natural(n):
    if(n == 1):
        return 1
    else:
        return (n + natural(n-1))
    
print(f"Sum upto {n} is {natural(n)}")