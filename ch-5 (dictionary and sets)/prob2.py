#Write a program to input eight numbers from the user and display all the unique 
# numbers (once). 

num = set()

for i in range(8):
    num.add(int(input("Enter your number: ")))
    
print(num)
for item in num:
    print(item)