# A class is a blueprint for creating object. 
class Employee:
    language = "Python" #language is class attribute
    salary = 14000000 #salary is class attribute
    
sagun = Employee() #Here sagun is an object
sagun.name = "Sagun" #name is object attribute or instance attribute
sagun.employeeId = '081067' #Adding instance attribute
print(sagun.name)
print(sagun.salary)
print(sagun.language)
print(sagun.employeeId)

aditya = Employee()
aditya.name = "Aditya" #name is object attribute or instance attribute
aditya.salary = 13000000
print(aditya.name)
print(aditya.salary)
print(aditya.language)

