'''
Create a class “Programmer” for storing information of few programmers 
working at Microsoft. 
'''
class Programmer:
    company = "Microsoft"
    
    def __init__(self,name,employeeId,salary,age):
        self.name = name
        self.employeeId = employeeId
        self.salary = salary
        self.age = age

a = Programmer("Sagun Kumar Bhagat",'081BCT',19028334,28)
print(a.name, a.age, a.employeeId, a.salary)

b = Programmer("Hari Krishna","BEI081",12334423,29)
print(b.name, b.age, b.employeeId, b.salary)
