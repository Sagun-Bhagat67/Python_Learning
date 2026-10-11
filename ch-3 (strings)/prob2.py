name = input("Enter your name: ")
Date = input("Enter a Date: ")

letter =('''
        Dear <|name|>,
        You are Selected!
        <|Date|>
        ''')
print(letter.replace("<|name|>",name).replace("<|Date|>",Date))
