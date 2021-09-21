# Import dependancies
import os
import shutil
from shutil import copyfile
from os import path

# This script will itterate through the files in the dir directory,
# and will rename them to the date located on line 2 index 5-12.

# This script was created by Andrew Rose for the purpose of renaming multiple files instantly
# without having to open them and check their dates


# Set Directory to whatever directory you would like to scan and have the
# names of the fils changed.
dir = "\\\\atlas\Accounting\\Optima Daily"
newDir = "\\\\tritium\\KenoDrop"
copyDir = "\\\\tritium\\KenoDrop\\Optima Archive"



os.chdir(dir)
for i in os.listdir():
    file = open(i, "r")
    firstLine = file.readline()
    secondLine = file.readline()
    newSecondLine = secondLine[5:13].split("/")
    newFileName = "Optima_" + newSecondLine[0] + "-" + newSecondLine[1] + "-" + newSecondLine[2]
    file.close()
    if path.exists(newDir + "\\" + newFileName + ".txt"):
        counter = 0
        print("THIS IS ONE: " + str(counter))
        while path.exists(newDir + "\\" + newFileName + "(" + str(counter) + ").txt"):
            counter += 1
            print(counter)
        shutil.move(dir + "\\" + i, newDir + "\\" + newFileName + "(" + str(counter) + ").txt")
        copyfile(newDir + "\\" + newFileName + "(" + str(counter) + ").txt", copyDir + "\\" + newFileName + "(" + str(counter) + ").txt")
    else:
        shutil.move(dir + "\\" + i, newDir + "\\" + newFileName + ".txt")
        copyfile(newDir + "\\" + newFileName + ".txt", copyDir + "\\" + newFileName + ".txt")
