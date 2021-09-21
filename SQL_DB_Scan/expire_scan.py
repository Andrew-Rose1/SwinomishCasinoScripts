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


port = 25  # For starttls
smtp_server = "internal.swinomishcasino.com"
sender_email = "*******@swinomishcasino.com"
sender_user = "NLC\"*******"
receiver_email = "*******@swinomishcasino.com"
password = *******


subject = "Track-It! -- Today's Closed Tickets!"
body = """
Here is a list of the tickets closed
{}
""".format(var2)

# make up message
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = receiver_email

#context = ssl.create_default_context()
print("sent")

with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    print("sent1")
    #server.starttls(context=context)
    server.starttls()
    server.ehlo()  # Can be omitted
    print("Attempting to login...")
    server.login(sender_user, password)
    print("Logged In!")
    server.sendmail(sender_email, receiver_email, msg.as_string())

print("sent")
