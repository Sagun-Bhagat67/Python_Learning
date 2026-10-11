# Write a python program using function to convert Celsius to Fahrenheit. 

celsius = float(input("Enter tempr in Celsius: "))
def convert(celsius):
    farenheit = (celsius*180)/100+32
    return farenheit
farenheit = convert(celsius)
print(f"{celsius} degree celsius = {round(farenheit,2)} degree farenheit")