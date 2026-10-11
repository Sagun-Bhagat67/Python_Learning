# Write a program to print multiplication table of a given number using for loop.
n = int(input("Enter a number for multiplication table: "))

print(f"\nMultiplication table of {n} is: \n ")
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")
    