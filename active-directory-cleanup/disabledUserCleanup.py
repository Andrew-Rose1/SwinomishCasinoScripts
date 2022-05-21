from ldap3 import Connection, SUBTREE
import os
import stat
import shutil
from email.mime.text import MIMEText
import smtplib

atlasUsersDir = "/mounts/atlas/Users"
minervaUsersDir = "/mounts/argus/Users"
argusUsersDir = "/mounts/minerva/Users"
lokiUsersDir = "/mounts/loki/Users"
listOfDirs = []
listOfDirs.append(atlasUsersDir)
listOfDirs.append(minervaUsersDir)
listOfDirs.append(argusUsersDir)
listOfDirs.append(lokiUsersDir)
archiveDir = "/mounts/loki/User_Home_Files"
names = []
keepNames = []


def on_rm_error(func, path, exc_info):
    try:
        os.chmod(path, stat.S_IWRITE)
        func(path)
    except Exception as exc:
        print("Skipped:", path, "because:\n", exc)


conn = Connection("*****", "NLC\\*****", "*****", auto_bind=True)
results = conn.extend.standard.paged_search(
    search_base='OU=.Keep,OU=Disabled,DC=NLC,DC=com',
    search_filter='(objectCategory=person)',
    search_scope=SUBTREE,
    attributes=['cn']
)
print("Connection to Domain Controller was Successful!")
for i in results:
    names.append(i['attributes']['cn'])


print("Scanning AD users... Please wait...")
print("------------------------------------------\n")


# Move names from root to Archived
size = 0
for name in names:
    seen = False
    for d in listOfDirs:
        os.chdir(d)
        arrName = name.split(' ')
        folderName = (arrName[0][0] + arrName[1]).lower()
        file = d + "/" + folderName
        if os.path.isdir(file):
            seen = True
            # Calculate file size
            for path, dirs, files in os.walk(file):
                for f in files:
                    fp = os.path.join(path, f)
                    size += os.path.getsize(fp)
            gbSize = size/1000000000
            size = 0
            if gbSize >= 1:
                printSize = str(gbSize) + " GB"
            else:
                printSize = str(size/1048576) + " MB"

            src = d + "/" + folderName
            dst = archiveDir + "/" + folderName
            # Move folders
            if (gbSize <= 5):
                print(
                    f'Moving folder {folderName} ({printSize})... Please wait...')
                shutil.copytree(src, dst)
                shutil.rmtree(src, onerror=on_rm_error)
                conn.modify_dn(f'cn={name},OU=Disabled,DC=nlc,DC=com', f'cn={name}',
                               new_superior='OU=.Archived,OU=Disabled,DC=nlc,DC=com')
                print(
                    f'Folder {folderName} moved to archive. {name} moved to archived OU.\n')
            else:
                keepNames.append(name)
                print(
                    f'{folderName} size is over 5GB! Moving folder {folderName} ({printSize}) and informing IT....')
                shutil.copytree(src, dst)
                shutil.rmtree(src, onerror=on_rm_error)
                print(
                    f'Folder {folderName} moved to archive. {name} moved to archived OU.\n')
    if not seen:
        print(f'Could not find user home folder for {name}\n')


print(f"\nScript complete! {len(names)} accounts affected.")
print(names)
if len(keepNames) > 0:
    print("\nThe following users were moved to the Keep OU in AD:")
    print(keepNames)
    try:
        port = 25 
        smtp_server = "internal.swinomishcasino.com"
        sender_email = "dbmail@swinomishcasino.com"
        sender_user = "NLC\dbmail"
        receiver_email = "it@swinomishcasino.com"
        password = "*****"

        subject = "Disabled OU Cleanup -- Keep Users"
        body = """
            The following users were moved to the Keep OU:
                {}
            """.format(keepNames)

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email

        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(sender_user, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent!")
    except:
        print("Email failure")
