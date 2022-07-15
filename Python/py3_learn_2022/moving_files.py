import os

source = "folder"
destination = "C:\\tmp\\folder"
try:
    if os.path.exists(destination):
        print("Ther is a file already")
    else:
        os.replace(source,destination) 
        print(source + " was moved")   
except FileExistsError as e:
    print("File not found")
