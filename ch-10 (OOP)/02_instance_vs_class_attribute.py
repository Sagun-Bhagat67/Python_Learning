# A class is a blueprint for creating object. 
class Employee:
    language = "Python" #language is class attribute
    salary = 14000000 #salary is class attribute
    
sagun = Employee() #Here sagun is an object
sagun.name = "Sagun" #name is object attribute or instance attribute
sagun.employeeId = '081067' #Adding instance attribute
sagun.language = 'JavaScript'
print(sagun.name)
print(sagun.salary)
print(sagun.language)
print(sagun.employeeId)

'''
Note: Instance attributes, take preference over class attributes during assignment & 
retrieval.
i.e. Instance attribute dominates class attribute
i.e. Instance attribute has high priority than class attribute
'''

