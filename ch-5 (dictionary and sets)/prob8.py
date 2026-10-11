#  Can you change the values inside a list which is contained in set S? 
# s = {8, 7, 12, "Harry", [1,2]} 

s = {8, 7, 12, "Harry", [1,2]} 

#Here we cannot update the list inside the set 
# Reasons :
#    We cannot assign a list inside a set 
#     A set can contain only hashable elements.

#     Lists are mutable, meaning their values can be changed.

#     Lists are unhashable, so they cannot be elements of a set.