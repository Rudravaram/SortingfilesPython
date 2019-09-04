
import os
import shutil

# provide the path where the files are stored
path  = "C:/Users/XXXXXXX/Desktop/Files/"

#this is to list out the files that are in that folder structure
names = os.listdir(path)

#Create the List of folders wher you want the extension files to me moved
folder_name = ['pdf','py','zip']

#Loop thu the path to check if the folder exists - if 'yes' then ignore if 'no' the create the folder
for x in range(0,3):
    if not os.path.exists(path+folder_name[x]):
        os.makedirs(path+folder_name[x])

#search for the file extensions and move the files according to the file extensions
for files in names:
    if ".pdf" in files and not os.path.exists(path+'pdf/'+files):
        shutil.move(path+files, path+"pdf/"+files)
    if ".py" in files and not os.path.exists(path+'py/'+files):
        shutil.move(path+files, path+"py/"+files)
    if ".zip" in files and not os.path.exists(path+'zip/'+files):
        shutil.move(path+files, path+"zip/"+files)
