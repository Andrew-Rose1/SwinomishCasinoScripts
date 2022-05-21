# Swinomish Casino & Lodge Scripts
An accumulation of the scripts I developed while working at Swinomish Casino and Lodge.
Some have been slightly modified since their deployment.

These scripts were made while closly working with the System Administrator/IT Manager and Database Analyst at Swinomish Casino & Lodge.

To better organzie my work, I created a Virtual Linux Machine (AUTOVM) to store and run the scripts that would be ran daily/weekly/monthly. The scripts were ran via crontjobs and would notify the appropriate department directors, via email, of the job's outcome. The scripts would also keep track of an output log (an example is included).

## Usage
Most of these scripts are ran via automation. In the cases users want to manually run a script, this is how it is done:
1. Python scripts can be ran manually on linux/unix machines (with python insatlled) with:

    ```sh
    python3 {PATH_TO_FILE}
    ```
    
2. For Windows machines (most of our end user computers), I would provide thme with a .exe by using pyinstaller.
  * Install pyinstaller
    ```sh
    pip install pyinstaller
    ```
  *
    ```sh
    pyinstaller --onefile {PATH_TO_FILE}
    ```
  * A "dist" folder wherver the command was ran. Inside there should be a standalone .exe.

## Atlas To Tritium
- Move files from one sever to another, and create a copy to be archived. The files would be renamed according to the date inside of the report.
- Ran daily and stored on the Virtual Linux Machine.
## CDS Export
- Used by all slot employees to copy the needed export report from a server to their local machines.
## ClubData CleanUp
- Scan the given directory and delete all folders except for the last two added.
- Ran daily and stored on the Virtual Linux Machine.
## Disable Active Sync
- A powershell script that prompts the user for a username of an account they wish to disable "email-on-phone" for. The user's "email-on-phone" access would then be revoked.
## LodgePMS
- ReviewPro and Strategy9. Similar to "Atlas To Tritium", this program will scan a folder and move specific files to another server.
- This script was ran daily and stored on the Virtual Linux Machine.
## Windows  Scan
- Scanned a device report from Endpoint Manager to find all Windows 10 machines that were below Windows build 2004. Then export these computers to a csv file that the IT technicians can use as a reference for Windows OS updates. 
## Warranties Scan
- A python script that uses SQL queries to check a database. This databse keeps track of all of our warranties for hardware and software. The script will find all warranties that are close to expiring and email the System Administrator of the ones it finds.
- Ran daily and stored on the Virtual Linux Machine.
## Slot Mix Reporting
- This script contains sensitive data and is still a work in progress
- Takes the companies' slot machine data for the week and compares it to threshold and average values. These numbers are placed in tables corresponding to the slot machine bank number and attached to a CAD drawing next to their respective bank.
- This is all done automatically with the execution of a script. This allowed my IT Manager and Slots Director to better visualize which slot machines are underperforming.
- Ran weekly and stored on the Virtual Linux Machine.
