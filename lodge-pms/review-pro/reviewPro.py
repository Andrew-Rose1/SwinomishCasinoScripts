# Import dependancies
import os
import shutil
from shutil import copyfile
from os import path
from datetime import date
# This script will itterate through the files in the dir directory,
# and will move them to the newDir. It will also ensure that if the filename
# already exists that it will append a number to the end of the name.



# Set Directory to whatever directory you would like to scan and have the
# names of the fils changed.
dir = "\\\\lodgepms\\MICROS\\opera\\export\\OPERA\\scl"
newDir = "\\\\lodgepms\\MICROS\\opera\\export\\OPERA\\scl\\reviewpro"

today = date.today()
d1 = today.strftime("%m-%d-%y")

os.chdir(dir)
for i in os.listdir():
    if (i[0:6] == 'survey'):
        if path.exists(newDir + "\\" + d1 + " " + i):
            counter = 1
            while path.exists(newDir + "\\" + "(" + str(counter) + ")" + d1 + " " + i):
                counter += 1
            shutil.move(dir + "\\"  + i, newDir + "\\" + "(" + str(counter) + ")" + d1 + " " + i)
        else:
            shutil.move(dir + "\\" + i, newDir + "\\" + d1 + " " + i)
