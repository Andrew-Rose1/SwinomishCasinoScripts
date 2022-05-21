import os
from datetime import datetime, timedelta
import time
import shutil


# dir = "\\\\clubdata\\repldata\\unc\\CLUBDATA_PKMS_PKMS SNAPSHOT REPLICATION"
dir = "C:\\Users\\arose\\Programs\\ClubdataCleanUp\\Test"

today = datetime.now()
print(today)

twoDaysBack = today - timedelta(days=2)
print(twoDaysBack)
for i in os.listdir(dir):
    try:
        year = int(i[:4])
        month = int(i[4:6])
        day = int(i[6:8])

        dateObj = datetime(year, month, day)
        if dateObj < twoDaysBack:
            shutil.rmtree(dir + "\\" + i)
            print("Removed: " + i)
    except:
        print("Error with file name: " + i)
