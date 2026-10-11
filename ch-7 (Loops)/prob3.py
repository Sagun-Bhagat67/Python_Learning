# Write a program to print multiplication table of a given number using while loop. 

n = int(input("Enter a number for multiplication table: "))

i =1

print(f"Multiplication table of {n} is: \n")
while(i<=10):
    print(f"{n} * {i} = {n*i}")
    i+=1