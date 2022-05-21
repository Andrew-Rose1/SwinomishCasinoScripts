import mysql.connector
from email.mime.text import MIMEText

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="*********",
  database="tracker"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT model_ver, expire FROM products WHERE 30 >= DATEDIFF(expire, CURRENT_DATE)")

for (model_ver, expire) in mycursor:
    vars = model_ver + " is expiring soon!   |   Expiration date: " + expire + "\n"


port = 25  
smtp_server = "internal.swinomishcasino.com"
sender_email = "*******@swinomishcasino.com"
sender_user = "NLC\"*******"
receiver_email = "*******@swinomishcasino.com"
password = *******

subject = "ATTENTION: WARRANTIES EXPIRING SOON"
body = """
Here is a list of warranties expiring soon:
{}
""".format(var2)

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = receiver_email

with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender_user, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())

