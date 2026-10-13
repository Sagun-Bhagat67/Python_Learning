'''
while opening a file, By default it will be open on read mode

while writing a file , it will create that file in same folder

Remember the file must be on same folder
'''

st = 'Hello World! This is Sagun Kumar Bhagat'

#open a file in write mode
f = open("file.txt",'w')
f.write(st)
f.close()

f = open("file.txt",'w')
f.write("I am a Developer....:>") #This line will overwrite the above written code 
f.close()

#file in reading mode

f = open("file.txt","r")
text = f.read()
print(text)
f.close()

f = open("main.txt",'r')
text = f.read()
print(text)
f.close()

#Lets try writing a existing file 
f = open("main.txt",'w')
f.write("So.... How is its all going\n") #This line will overwrite the above written code 
f.write("How's Its Going Dude!!!")
f.close()

#Open in append mode
f = open("file.txt","a")
f.write("This was aaded at the end of file...") #This will append at the end of current file
f.close()

f = open("main.txt",'r')
txt = f.read() 
print(txt)
f.close()

f = open("file.txt",'r')
txt = f.read() 
print(txt)
f.close()