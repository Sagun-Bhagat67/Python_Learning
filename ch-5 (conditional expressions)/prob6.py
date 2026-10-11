# Write a program to calculate the grade of a student from his marks from the 
# following scheme: 
# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50        
# => F 

mark = int(input("Enter the mark: "))
if(mark>=90 and mark<=100):
    print("Your Grade is Excellent")
elif(mark>=80 and mark<90):
    print("Your Grade is A")
elif(mark>=70 and mark<80):
    print("Your Grade is B")
elif(mark>=60 and mark<70):
    print("Your Grade is C")
elif(mark>=50 and mark<60):
    print("Your Grade is D")
elif(mark>=0 and mark<50):
    print("Your Grade is F (Fail)!!!!.")
    
else:
    print("Enter valid marks")
    