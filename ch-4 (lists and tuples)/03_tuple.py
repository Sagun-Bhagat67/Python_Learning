a = (1,3,2,5,7,2,4,3,2,1,2,1,"Sagun",True)
print(type(a))
no = a.count(1) #It counts the total occurance of 1 in Tuple a
print(no)

i = a.index(2) #it will return the index of value 2 in tuple a (it will terminate once it encounter the value , its doesn't go to end)
print(i)

b = ("Ram","Shyam","Hari","Gita","Sagun")
print(b.index("Sagun"))

#Tuples Method 
c = (1,2,4,6,3,45,23,67,89)
print(sorted(c))
print(sum(c))
print(min(c))

print(2 in c)

d = (1,2,3)
e = d*3
print(e)