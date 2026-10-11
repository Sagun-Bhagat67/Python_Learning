# Write a python function which converts inches to cms. 
# 1 inch = 2.54cm 

inch = float(input("Entr inches: "))

def convert(inch):
    return inch*2.54

print(f"{inch} inches = {convert(inch)} cm")