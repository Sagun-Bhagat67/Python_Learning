'''
__init__() is a special method which is first run as soon as the object is created. 
__init__() method is also known as constructor. 
It takes 'self' argument and can also take further arguments. 
'''

class Employee:
    salary =1230000 
    language = "Python" 
    
    def getInfo(self):
        print(f"Hii\nYour name is {self.name}\nYour salary is {self.salary}\nYou choose {self.language} Language")
        
    def __init__(self): #dunder method which is automatically called 
        print("I am creating an object\nI am dunder method")
    def greet(self): 
        print("Good Morning")
       
    @staticmethod  # decorator to mark noon as a static method 
    def noon():
        print("Have a nice Day!!")
        
sagun = Employee() #This line will first rin __init__
sagun.name = "Sagun Kumar Bhagat"
sagun.salary = 14000000 #instance attribute

sagun.greet()
Employee.getInfo(sagun)
sagun.noon()

rohan = Employee() #This line will again run __init__ 