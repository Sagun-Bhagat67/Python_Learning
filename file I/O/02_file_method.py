f = open("my_file.txt") #By default it will open on read mode 
'''
lines = f.readlines() # This will read all the lines of code present there 
print(lines,type(lines))
'''

'''

line1 = f.readline() #This will read single line and cursor move to nxt line so that next readline() statement can read that line 
print(line1,type(line1))

line2 = f.readline()
print(line2,type(line2))

line3 = f.readline()
print(line3,type(line3))

line4 = f.readline()
print(line4,type(line4))

line5 = f.readline()
print(line5,type(line5))

line6 = f.readline()
print(line6 == "")
'''

line = f.readline() #This will read a single line
while(line != ""): #Checks if the line comes to end or not
    print(line) #This will print the current line
    line = f.readline() #Control of line move to next line
    
f.close()