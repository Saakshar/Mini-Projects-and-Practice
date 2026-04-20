import os
import shutil
user = input("enter the name of your user")
location = input("enter the file path for the files you would like to store under the folder on your desktop titled 'Coding Files' *also remember to replace all backslashes with forward slashes*: ")
location = location + '/'
files = os.listdir(location)
for file in files:
    shutil.move((location+file), "C:/Users/"+str(user)+"/OneDrive\Desktop/Coding Files/")