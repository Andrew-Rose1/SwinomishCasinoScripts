# Import dependancies
import os
from os import path
import shutil
from shutil import copyfile
import time

# This script was created by Andrew Rose for the purpose of copying a directory.

# Set Source and  Directory
src = "\\\\Atlas\\Common\\CDS-Export\\Drive E"
dest = "c:\\CDS-Export\\Drive E"

# Copy Source directory to destination
if os.path.isdir(dest):
    shutil.copy(src + "\\CDS.bak", dest)
else:
    shutil.copytree(src, dest)

print("Copy successful!")
time.sleep(10)
