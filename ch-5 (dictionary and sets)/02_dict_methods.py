marks = {
    "Sagun":98,
    "Aditya":97,
    "Prithivi":96,
    "Krishna":95,
    "Name":"Rakesh Mehta"
}

print(marks["Sagun"]) #Returns value at key "Sagun"

print(marks.items()) # returns all key-value pair in tuples
print(marks.keys()) # returns all keys in a list inside a tuple 
print(marks.values())
marks.update({"Sagun":99}) # update the key "Sagun"
print(marks)

print(marks.get("Name")) #returns the value at key "Name"

print(marks.get("Shivaji")) # returns None

print(marks["Shivaji"]) #returns an error 