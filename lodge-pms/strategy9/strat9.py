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
# dir = "\\\\lodgepms\\d$\\MICROS\\opera\\export\\OPERA\\scl"
# newDir = "\\\\BAYESIAN\\scl\\Strategy9"
# archiveDir = "\\\\BAYESIAN\\scl\\Strategy9\\Archive"

dir = "C:\\Users\\arose\\Programs\\LodgePMS\\Strategy9"
newDir = "C:\\Users\\arose\\Programs\\LodgePMS\\Strategy9\\newLoc"
archiveDir = "C:\\Users\\arose\\Programs\\LodgePMS\\Strategy9\\newLoc\\Archive"


#
# today = date.today()
# d1 = today.strftime("%m-%d-%y")
#
# os.chdir(dir)
# for i in os.listdir():
#     if (i[0:8] == 'strategy') or (i[0:8] == 'stragety'):
#         if (i.endswith('.txt')):
#             if path.exists(newDir + "\\" + d1 + " " + i):
#                 counter = 1
#                 while path.exists(newDir + "\\" + "(" + str(counter) + ")" + d1 + " " + i):
#                     counter += 1
#                 shutil.move(dir + "\\"  + i, newDir + "\\" + "(" + str(counter) + ")" + d1 + " " + i)
#                 copyfile(newDir + "\\" + "(" + str(counter) + ")" + d1 + " " + i, archiveDir + "\\" + "(" + str(counter) + ")" + d1 + " " + i)
#             else:
#                 shutil.move(dir + "\\" + i, newDir + "\\" + d1 + " " + i)
#                 copyfile(newDir + "\\" + d1 + " " + i, archiveDir + "\\" + d1 + " " + i)


os.chdir(dir)
for i in os.listdir():
    if (i[0:8] == 'strategy') or (i[0:8] == 'stragety') or (i[0:7] == 'stategy'):
        if (i.endswith('.txt')):
            with open(i, 'r') as f:
                last_line = (f.readlines()[-2]).split("\t")
                last_line_date = last_line[6]
                f.close()
            if path.exists(newDir + "\\" + last_line_date + " " + i):
                counter = 1
                while path.exists(newDir + "\\" + "(" + str(counter) + ")" + last_line_date + " " + i):
                    counter += 1
                shutil.move(dir + "\\"  + i, newDir + "\\" + "(" + str(counter) + ")" + last_line_date + " " + i)
                copyfile(newDir + "\\" + "(" + str(counter) + ")" + last_line_date + " " + i, archiveDir + "\\" + "(" + str(counter) + ")" + last_line_date + " " + i)
            else:
                shutil.move(dir + "\\" + i, newDir + "\\" + last_line_date + " " + i)
                copyfile(newDir + "\\" + last_line_date + " " + i, archiveDir + "\\" + last_line_date + " " + i)

# dir = "C:\\Users\\arose\\Programs\\LodgePMS\\Strategy9"
# os.chdir(dir)
# for i in os.listdir():
#     if (i.endswith('.txt')):
#         print(i)
#         with open(i, 'r') as f:
#             last_line = (f.readlines()[-2]).split("\t")
#             last_line = last_line[6]
#             f.close()
#             # last_line_delim = last_line.split("\t")
#         print(last_line)
