import os
from datetime import datetime, timedelta
import time
import shutil
from email.mime.text import MIMEText
import smtplib



dir = "//mounts//synerion//PDSExport"
copyDir = "//mounts//synerion//Archive"
today = datetime.now().date()

port = 25
smtp_server = "internal.swinomishcasino.com"
sender_email = "dbmail@swinomishcasino.com"
sender_user = "NLC\dbmail"
receiver_email = "it@swinomishcasino.com"
password = "********"

f = open("/scripts/outputLog.txt", "a")
try:
    for i in os.listdir(dir):
        if i.lower().endswith(".csv"):
            print(i)
            shutil.copyfile(dir + "//" + i, copyDir + "//" + i[0:-4] + "_" + str(today) + ".CSV")
    f.write("[Success] -- cleanUp.py ran at " + str(datetime.now()) + "\n")

    subject = "Event SUCCESSFUL: Synerion Copy"
    body = """
    [SUCCESSFUL JOB]

    Event Name: Synerion Copy
    Event Type: Run Application
    Ended at: {}

    """.format(str(datetime.now().strftime('%m/%d/%Y %H:%M')))

except:
    f.write("[FAILURE] -- synerionCopy.py tried to run at " + str(datetime.now()) + "\n")

    subject = "Event FAILURE: Synerion Copy"
    body = """
    [FAILED JOB]

    Event Name: Synerion Copy
    Event Type: Run Application
    Ended at: {}

    """.format(str(datetime.now().strftime('%m/%d/%Y %H:%M')))
f.close()


msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = receiver_email
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()
    server.login(sender_user, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
print("Email sent!")

