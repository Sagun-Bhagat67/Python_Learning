#Pass--> It instructs the compiler to do nothing 

for i in range(1000):
    pass

#This pass satatement let you run your below code with above for loop being on the code 
# If we haven't used pass statement above then it will show us indentation error 


#Break says--> Exit the loop right now 
for i in range(100):
    if(i==25):
        break
    print(i)
else:
    print('Done for Break statement....\n') #This line will not executed as above line of code encounter break it will just get out of loop
    
#Continue says--> skip this Iteration and go for next iteration
for i in range(50,60):
    if(i==55):
        continue
    print(i)
else:
    print("Done for Continue statement...!!\n")
    