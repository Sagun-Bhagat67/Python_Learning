'''
self refers to the instance of the class. It is automatically passed with a function call 
from an object.
'''


class Employee:
    salary =1230000 #class attribute
    language = "Python" #class attribute
    
    def getInfo(self): #self is a parameter that it takes (usually it is written self, You can write anything)
        print(f"Hii\nYour name is {self.name}\nYour salary is {self.salary}\nYou choose {self.language} Language")
        
    def greet(self): #No matter you use self or not inside function, but you need to give this parameter
        print("Good Morning")
        
        """
        Sometimes we need a function that does not use the self-parameter. We can define a 
        static method like this: 
        """
    @staticmethod  # decorator to mark noon as a static method 
    def noon():
        print("Have a nice Day!!")
        
sagun = Employee()
sagun.name = "Sagun Kumar Bhagat"
sagun.salary = 14000000 #instance attribute

sagun.greet()
Employee.getInfo(sagun) #This line is equivalent sagun.getInfo()
# sagun.getInfo() ==> Employee.getInfo(sagun)
sagun.noon()