'''
 Create a class with a class attribute a; create an object from it and set ‘a’ 
directly using ‘object.a = 0’. Does this change the class attribute?
'''
class Hello:
    a = 234
    
num = Hello()
print(f"before instance atttribute: {num.a}") #This prints class attribute because instance attribute is no present

num.a = 0

print(f"After instance attribute: {num.a}") #This prints instance attribute because instance attribute set

print(f"The class attribute is: {Hello.a}") #This directly prints the class attribute from class Hello
'''
The question asks: Does this change the class attribute?

The answer is: No

Because The instance attribute is only iunstance, If we again print Hello.a then we get the original value  
'''
