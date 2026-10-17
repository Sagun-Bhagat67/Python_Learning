'''
Write a class “Calculator” capable of finding square, cube and square root of a 
number. 
'''
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
