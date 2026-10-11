#  Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user.

mark1 = float(input("Enter mark of subject 1: "))
mark2 = float(input("Enter mark of subject 2: "))
mark3 = float(input("Enter mark of subject 3: "))

avg = ((mark1+mark2+mark3)/300)*100

if(avg>40 and mark1>=33 and mark2>=33 and mark3>=33):
    print("You have passed your exam....!!")
    
else:
    print("You have failed your exam....!!")