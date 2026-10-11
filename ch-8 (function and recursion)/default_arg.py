# In default aprameter if the argument is not passed then it uses the default value else it uses the passed value

def greet(name="Prithivi",end ="have a nice day"):
    print(f"Hello {name}.\n{end}")
    
greet("Sagun")

name = input("Enter your name: ")
greet(name,"Slute xa twlai")
greet(name,"Vai hos re tw mero")
greet(name)