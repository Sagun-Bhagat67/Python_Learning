p1 = 'Make a lot of money'
p2 = 'buy now'
p3 = 'click this'
p4 = 'subscribe this'

comment = input("Enter your comment: ")

if(p1 in comment or p2 in comment or p3 in comment or p4 in comment):
    print("Spam message........!!!!!!!!")
else:
    print(comment)
