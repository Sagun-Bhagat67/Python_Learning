import os
# Select the folder path you want to explore
directory_path = 'D:\\Learning python'

# Read the content of the folder you select and store it to the variable named content
content =os.listdir(directory_path)

for item in content:
    print(item)
    
