# Swinomish Casino & Lodge Scripts
An accumulation of the small scripts I made while working at Swinomish Casino and Lodge.
Some have been slightly altered since their deployment.

These scripts were made while closly working with the System Administration/IT Manager and Database Analyst at Swinomish Casino and Lodge.

To better organzie my work, I created a Virtual Linux Machine (AUTOVM) to store and run the scripts that would be ran daily/weekly/monthly. The scripts were ran via crontjobs and would email the appropriate department directors if the job ran successfully or failed. The scripts would also keep track of an outputLog (an example is included).

## Atlas To Tritium Transfer
- Script to move files from one sever to another, and create a copy to be archived. The files would be renamed according to the date inside of the report.
- This script was ran daily and stored on the Virtual Linux Machine.
## CDS Export
- Script that was used by all slot employees to copy the needed export report from a server to their local machine.
## ClubData CleanUp
- Script that would scan the given directory and delete all folders except for the last two added.
- This script was ran daily and stored on the Virtual Linux Machine.
## Disalbe ActiveSync
- A powershell scrip that prompt the user for a username of the person's account they wanted to disable email-on-phone for. The user's email-on-phone access would then be revoked.
## LodgePMS
- ReviewPro and Strategy9. Similar to "Atlas To Tritium Transfer", this program will scan a folder and move specific files to another server.
- This script was ran daily and stored on the Virtual Linux Machine.
## Windows 2004 Scan
- A script that scanned a device report from Endpoint Manager to find all Windows 10 machines that were below Windows build 2004. It would then export these computers to a csv file for the IT Department technicians to use as a reference sheet for Windows OS updates. 
## SQL DB Scan
- A python script I created for my System Administrator that uses SQL queries to check a databse. The databse that it checks keeps track of all of our warranties for hardware and software. The script will find all warranties that are close to expiring and email the System Administrator of the ones it finds.
- This script was ran daily and stored on the Virtual Linux Machine.
## SlotMixReporting
- This script contains sensitive data and is still a work in progress
- Basically it takes the companies slot machine data for the week and compares it to threshold and avergae values. These numbers are placed in tables corresponding to the slot machine bank number and attatched to a CAD drawing next to their respective bank.
- This is all done automatically with the execution of a script. This allowed my IT Manager and Slots Director to better visualize which slot machines are underperforming.
- This script was ran weekly and stored on the Virtual Linux Machine.
