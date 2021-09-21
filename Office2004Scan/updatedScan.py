from datetime import datetime, timedelta
import os
import csv

path = '\\\\loki\\IT Dept\\Microsoft Licensing\\VersionScan\devicelist.csv'
export_path = '\\\\loki\\IT Dept\\Microsoft Licensing\\VersionScan\\needed_upgrades.csv'

if os.path.exists(export_path):
    os.remove(export_path)

file = open(path, "rU")
reader = csv.reader(file, delimiter=',')
# file2 = open(export_path, "w", newline='')
# writer = csv.writer(file2, delimiter=',')
#
# writer.writerow(['Name', 'OS', 'Version'])
# for row in reader:
#     # Name: Column 2
#     # OS Name: Column 11
#     # OS Version: Column 12
#         # OS Version 2004 = 10.0.19041
#     if "Microsoft" in row[11] and row[12] < "10.0.19041":
#         print("Name: " + row[2] + "  |  OS: " + row[11] + "  |  Version: " + row[12])
#         writer.writerow([row[2], row[11], row[12]])
modifiedDateUNIX = os.path.getmtime(path)
modifiedDateStr = datetime.utcfromtimestamp(modifiedDateUNIX).strftime('%Y-%m-%d %H:%M:%S')
modifiedDateObj = datetime.strptime(modifiedDateStr, '%Y-%m-%d %H:%M:%S').date()
print(modifiedDateObj)
for row in reader:
    try:
        dateObj = datetime.strptime(row[10][:10], "%Y/%m/%d").date()
        print(row[10])
        print(dateObj)
        print(type(dateObj))
        if dateObj > modifiedDateObj - timedelta(days=14):
            print("IS ACTIVE")
        else:
            print("NOT ACTIVE")
        print('\n')

    except:
        print("CANNOT DO THAT")
