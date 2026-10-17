class Employee:
    name = "Sagun Kumar Bhagat"
    salary = 12345678
    
    def __init__(self,name,salary,language):
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object.")
        
    def getInfo(self):
        print(f"My name is {self.name}\tMy slaary is {self.salary}\tMy language is {self.language}")
        
sagun = Employee("Sagun",123980765,"Python")
# sagun.name = "Sagun Bhagat"
sagun.getInfo()

sagar = Employee("Sagar",1223334,"JavaScript")
sagar.getInfo()