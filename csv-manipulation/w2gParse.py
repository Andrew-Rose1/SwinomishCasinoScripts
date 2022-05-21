import csv
import os
from datetime import datetime, timedelta


yesterday = datetime.today() - timedelta(days=1)
day = yesterday.day
month = yesterday.month
year = yesterday.year
monthString = yesterday.strftime("%b").upper()

root_loc = "/mounts/W2G/2022 W2G/EVERI/" + monthString
file_name = str(month) + "-" + str(day) + ".csv"
new_file_name = "new_" + file_name


try:
    os.chdir(root_loc)
    if file_name.endswith('.xlsx'):
        pass
    elif file_name.endswith('.csv'):
        headerLine = None
        with open(file_name) as f:
            csvReader = csv.reader(f)
            csv_out = open(new_file_name, 'w')
            csvWriter = csv.writer(csv_out)
            headers = {}
            for row in csvReader:
                if row[0] == "Winner's Tax Id No.":
                    headerLine = csvReader.line_num
                    for col in range(0, len(row)):
                        headers[row[col]] = col
                    # print(headers)
                    headers["Window"] = headers["Type Of Wager"]+1
                    row.insert(headers["Window"], "Window")
                    # print(headers)
                    row.pop(headers["Winner's Last Name"])
                elif headerLine != None:
                    if row[1] == "":
                        csvEOF_line = csvReader.line_num
                        row.pop(headers["Winner's Last Name"])
                    else:
                        # Combine first name and last name into first name column
                        fName = row[headers["Winner's First Name"]]
                        lName = row[headers["Winner's Last Name"]]
                        row[headers["Winner's First Name"]] = lName + ", " + fName

                        # Change Type of Column to numerica value
                        # Create new value for Window Value
                        typeOfCell = row[headers["Type Of Wager"]]
                        newTypeOfWindow = row[headers["Window"]]
                        if typeOfCell.lower() == "slot":
                            newTypeOf = 7
                            newTypeOfWindow = 'SDS'
                        elif typeOfCell.lower() == "keno":
                            newTypeOf = 5
                            newTypeOfWindow = 'KENO'
                        elif typeOfCell.lower() == 'table games' or typeOfCell.lower() == 'table game':
                            newTypeOf = 9
                            newTypeOfWindow = 'TG'
                        else:
                            newTypeOf = typeOfCell
                        row[headers["Type Of Wager"]] = newTypeOf

                        # Cashier column to 2 initials
                        cashierCell = row[headers["Cashier"]]
                        row[headers["Cashier"]] = cashierCell[:2].upper()

                        # Make indexing changes to row before writing
                        row.insert(headers["Window"], newTypeOfWindow)
                        row.pop(headers["Winner's Last Name"])
                csvWriter.writerow(row)

        # Archive original and rename new file to original name
        if not os.path.exists('archive'):
            os.mkdir('archive')
        os.rename(file_name, "archive/original_" + file_name)
        os.rename(new_file_name, file_name)

        f = open("/scripts/outputLog.txt", "a")
        f.write("[Success] -- w2g.py ran at " + str(datetime.now()) + "\n")
        f.close
    elif file_name.endswith('.xls'):
        pass
    else:
        pass
        f = open("/scripts/outputLog.txt", "a")
        f.write("[NO CHANGE] -- w2g.py ran at " + str(datetime.now()) + "\n")
        f.close
except Exception as e:
    f = open("/scripts/outputLog.txt", "a")
    f.write("[Failure] -- w2g.py ran at " + str(datetime.now()) +
            "with the following error: " + str(e) + "\n")
    f.close
    print("ERROR" + str(e))
