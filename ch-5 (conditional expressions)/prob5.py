# Write a program which finds out whether a given name is present in a list or not.
names = ["ram","Shyam","Hari","Gita","Binita","Babita","Sagun","Rakesh","Prashant","Aditya","Prithivi"]

name = input("Enter a name: ")

if (name in names):
    print(name,"is in the list")
else:
    print(name,"Is not in the list")