import imp
import os
import shutil


path = "folder"
try:
  #  os.remove(path)
  #  os.rmdir(path)
  shutil.rmtree(path)
except FileExistsError:
    print("File was not found")
except OSError :
    print("You cannot use that function to delete")
else:
    print(path + " was removed")
finally:
    print("This will be executed")
