# Write a program to greet all the person names stored in a list ‘l’ and which starts 
# with S. 
# l = ["Harry", "Soham", "Sachin", "Rahul"]
l = ["Harry", "Soham", "Sachin", "Rahul",'Sagun']

for item in l:
    if(item.startswith('S')):
        print("Good Morning",item)