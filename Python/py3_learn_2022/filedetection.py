import os

path = "C:\\Users\\Carl\\Desktop\\folder"

if os.path.exists(path):
    print("Thats a valid location")
    if os.path.isfile(path):
        print("that is a file")
    elif os.path.isdir(path):
        print("that is a folder")
else:
    print("Invalid location")

