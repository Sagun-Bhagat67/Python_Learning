'''
 Add a static method in problem 2, to greet the user with hello. 
 
 Solution to prob2 is below!!
 
 class Calculator:
    def __init__(self,number):
        self.number =number
        
    def square(self,number):
        print(f"Square of {number} is {number**2}")
        
    def cube(self,number):
            print(f"Cube of {number} is {number**3}")
    
    def squareroot(self,number):
            print(f"Squareroot of {number} is {number**(1/2)}")

n = int(input("Enter a number: "))

a = Calculator(n)
a.square(n)
a.cube(n)
a.squareroot(n)    

'''

class Calculator:
    def __init__(self,number):
        self.number =number
        
    @staticmethod
    def square(number):
        print(f"Square of {number} is {number**2}")
    
    @staticmethod    
    def cube(number):
            print(f"Cube of {number} is {number**3}")
    
    @staticmethod
    def squareroot(number):
            print(f"Squareroot of {number} is {number**(1/2)}")
    @staticmethod
    def greet():
        print("Hello World!!")

n = int(input("Enter a number: "))

a = Calculator(n)
a.greet()
a.square(n)
a.cube(n)
a.squareroot(n)    
