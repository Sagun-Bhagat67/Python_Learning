#Program to store marks of students and print them in sorted manner 
marks = []

for i in range (6):
    marks.append(int(input(f"Enter mark of student {i+1}:  ")))
    
print(marks)
marks.sort()
print(marks)