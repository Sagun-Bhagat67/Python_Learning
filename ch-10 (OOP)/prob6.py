'''
Can you change the self-parameter inside a class to something else (say 
“harry”). Try changing self to “slf” or “harry” and see the effects. 
'''

class Hello:
    def __init__(harry,name):
        harry.name = name
        print("Running......")
        
    def greet(harry):
        print(f"Hello {harry.name}")
        
a = Hello("Sagun Kumar Bhagat")
a.greet()

'''
The answer to above question is Yes.
Yes we can change the name of self parameter as we like
but writing self in self parameter is good practise

'''
