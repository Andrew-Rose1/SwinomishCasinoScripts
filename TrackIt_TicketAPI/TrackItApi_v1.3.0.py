import requests
import json
from tkinter import *
import os
import os.path
from os import path
from datetime import datetime
import tkinter.font as font
from tkinter.messagebox import showinfo
import ctypes


# TODO:
# 1) Allow user to choose sorting method
# 2) Check if current bearer key is valid, if not then rerun authorize()
# 3) Change date format to MM-DD-YYYY


### ChangeLog ###
# v1.2.0
#   Converted program to object oriented design
#   Created authorize function
#   Created gatherTickets function
#   Added version label
#   Added countdown timer
#   Changed some fonts
#
# v1.2.1
#   Added sorting method: "Priority, Date Opened"
#   Added sorting method identifying label
#
# v1.2.2
#   Moved category under ticket number with smaller text
#   Added number of notes per ticket
#   Chnaged background to darker gray, amd ticket color from blue to lighter gray
#   Slighly increased font


class Ticket:
    def __init__(self, ticket, count):
        self.notes = count

        try:
            self.id = str(ticket["Ticket"]["1"]["Value"])
        except:
            self.id = "N/A"

        try:
            self.open = str(ticket["Ticket"]["12"]["Value"])[:10]
        except:
            self.open = "N/A"

        try:
            self.summary = ticket["Ticket"]["22"]["Value"]
        except:
            self.summary = "N/A"

        try:
            self.addInfo = ticket["Ticket"]["7"]["Value"]
        except:
            self.addInfo = "N/A"

        try:
            self.category = ticket["Ticket"]["72"]["Value"]
        except:
            self.category = "N/A"

        try:
            self.priority = str(ticket["Ticket"]["107"]["Value"])[0]
            if self.priority == "H":
                self.priority = "2"
            elif self.priority == "M":
                self.priority = "3"
            elif self.priority == "L":
                self.priority = "4"
        except:
            self.priority = ""

        try:
            self.status = ticket["Ticket"]["96"]["Value"]
        except:
            self.status = "N/A"

        try:
            self.requestor= ticket["Ticket"]["149"]["Value"]
        except:
            self.requestor = "N/A"

        try:
            self.openedBy = ticket["Ticket"]["177"]["Value"]
        except:
            self.openedBy = "N/A"

        try:
            self.assigned = ticket["Ticket"]["157"]["Value"]
        except:
            self.assigned = "N/A"


class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("IT Department Open Tickets")
        self.versionNumber = "1.3.0"

        # Define final constants
        self.sortFont = font.Font(size=18, family='Helvetica', weight='bold')
        self.timerFont = font.Font(size=22, family='Helvetica', weight='bold')
        self.versionFont = font.Font(size=9, family='Helvetica')

        self.headerFont = font.Font(size=16, family='Helvetica', weight='bold')
        self.displayNameFont = font.Font(size=13, family='Calibri', weight='bold')
        self.valueFont = font.Font(size=13, family='Calibri')
        self.valueFont2 = font.Font(size=11, family='Calibri')
        self.rootColor = "gray10"
        self.color = "gray25"
        self.openTickets = []


        self.init_window()

    def authorize(self):
        mydata = {
          "grant_type": "password",
          "username": "SYSTEM ADMINISTRATION\WEBAPI",
          "password": "AA7Aj80"
        }
        token = requests.get("http://10.0.6.8/TrackIt/WebApi/token", data=mydata)
        print(token.json())
        bearerToken = token.json()["access_token"]

        myHeader = {
          "Authorization": "Bearer " + bearerToken
        }
        return myHeader

    def gatherTickets(self, myHeader):
        self.openTickets.clear()
        for i in range(340, 1000):
            url = 'http://10.0.6.8/TrackIt/WebApi/tickets/' + str(i)
            response = requests.get(url, headers=myHeader)
            if response:
                ticketJSON = response.json()
                if ticketJSON["Ticket"]["96"]["Value"] == "Open":
                    url2 = 'http://10.0.6.8/TrackIt/WebApi/tickets/' + str(i) + '/Notes/0/0'
                    response2 = requests.get(url2, headers=myHeader)
                    ticketCountJSON = response2.json()
                    self.openTickets.append(Ticket(ticketJSON, ticketCountJSON["Count"]))
        self.quickSort(self.openTickets, 0, len(self.openTickets)-1)


    def partition(self, arr, low, high):
        i = (low-1)
        pivot = arr[high].priority
        for j in range(low, high):
            if arr[j].priority != "" and pivot != "":
                if int(arr[j].priority) <= int(pivot):
                    i = i+1
                    arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)

    def quickSort(self, arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:
            pi = self.partition(arr, low, high)
            self.quickSort(arr, low, pi-1)
            self.quickSort(arr, pi+1, high)


    def countdown(self, time):
        minutes = time // 60
        seconds = time % 60
        if seconds < 10:
            seconds = "0" + str(seconds)
        self.cdLabel['text'] = "Refreshing in: " + str(minutes) + ":" + str(seconds)

        if time > 0:
            root.after(1000, self.countdown, time-1)
        else:
            self.cdLabel['text'] = "Refreshing..."
            self.init_window()


    def init_window(self):

        # Authorize and grab open tickets
        authorizedHeader = self.authorize()
        self.gatherTickets(authorizedHeader)

        # Remove old ticket frames
        for widget in root.winfo_children():
                widget.destroy()
        print("Screen Refreshed")


        rcounter = 0
        ccounter = 0
        for t in self.openTickets:
            if t.priority == "1":
                pcolor = "red3"
            elif t.priority == "2":
                pcolor = "darkorange2"
            elif t.priority == "3":
                pcolor= "yellow2"
            elif t.priority == "4":
                pcolor= "deepskyblue2"
            elif t.priority == "5":
                pcolor= self.color
            else:
                pcolor = self.color


    # Ticket Frame
            frame1 = Frame(root,bg=self.color,width=374,height=264,padx=3,pady=3)
            frame1.grid(row=rcounter, column=ccounter, padx=5,pady=3)


    # Ticket ID Label
            label = Label(frame1, text="Ticket " + t.id, bg=self.color, fg="white")
            label['font'] = self.headerFont
            label.place(x=115,y=1)


    # Category Label
            frame2 = Frame(frame1,bg=self.color,width=150,height=20,padx=1,pady=1)
            frame2.place(x=95, y=28)
            frame2.pack_propagate(False)

            label2 = Label(frame2, text=t.category, wraplength= 250,bg=self.color, fg="white", pady=0)
            label2['font'] = self.versionFont
            label2.pack()


    # Priority Label
            label0 = Label(frame1, text= t.priority, bg=pcolor)
            label0['font'] = self.headerFont
            label0.place(x=5,y=1)


    # Date Label
            label2 = Label(frame1, text="Opened:", wraplength= 250,bg=self.color, fg="white")
            label2['font'] = self.valueFont2
            label2.place(x=295,y=0)

            label0 = Label(frame1, text= t.open, bg=self.color, fg="white")
            label0['font'] = self.valueFont2
            label0.place(x=287,y=19)


    # Summary Label
            label1 = Label(frame1, text="Summary: ",bg=self.color, fg="white", pady=0)
            label1['font'] = self.displayNameFont
            label1.place(x=7,y=48)

            label2 = Label(frame1, text=t.summary,wraplength= 250,bg=self.color, justify="left", fg="white", pady=0)
            label2['font'] = self.valueFont
            label2.place(x=115,y=48)


    # Requestor Label
            label1 = Label(frame1, text="Requested by: ",bg=self.color, fg="white", pady=0)
            label1['font'] = self.displayNameFont
            label1.place(x=7,y=118)

            label2 = Label(frame1, text=t.requestor,bg=self.color, fg="white", pady=0)
            label2.place(x=140,y=118)
            label2['font'] = self.valueFont


    # Opened Label
            label1 = Label(frame1, text="Opened by: ",bg=self.color, fg="white", pady=0)
            label1['font'] = self.displayNameFont
            label1.place(x=7,y=139)

            label2 = Label(frame1, text=t.openedBy,bg=self.color, fg="white", pady=0)
            label2.place(x=140,y=139)
            label2['font'] = self.valueFont


    # Assigned Label
            label1 = Label(frame1, text="Assigned to: ", bg=self.color, fg="white", pady=0)
            label1['font'] = self.displayNameFont
            label1.place(x=7,y=160)

            label2 = Label(frame1, text=t.assigned, bg=self.color, fg="white", pady=0)
            label2.place(x=140,y=160)
            label2['font'] = self.valueFont

    # Info Label
            label1 = Label(frame1, text="Additional Info: ", bg=self.color, fg="white", pady=0)
            label1['font'] = self.displayNameFont
            label1.place(x=7,y=185)

            frame3 = Frame(frame1,bg=self.color,width=350,height=90,padx=1,pady=1)
            frame3.place(x=20, y=205)

            label2 = Label(frame3, text=t.addInfo, wraplength= 350, bg=self.color, justify="left", fg="white", pady=0)
            label2['font'] = self.valueFont2
            label2.pack()


    # Note Count Label
            label1 = Label(frame1, text="Number of Notes:  " + str(t.notes), bg=self.color, fg="white", pady=0)
            label1['font'] = self.valueFont2
            label1.place(x=237,y=240)


            rcounter += 1
            if rcounter > 3:
                ccounter +=1
                rcounter = 0


# Sorting Label
        self.sortLabel = Label(root, text="Sorting method:", fg="white", bg=self.rootColor, justify="right")
        self.sortLabel['font'] = self.sortFont
        self.sortLabel.place(x=1700, y=20)

        self.sortLabel = Label(root, text="Priority, Date Opened", fg="white", bg=self.rootColor, justify="right")
        self.sortLabel['font'] = self.sortFont
        self.sortLabel.place(x=1640, y=52)


# Countdown Timer
        self.cdLabel = Label(root, fg="white", bg=self.rootColor)
        self.cdLabel['font'] = self.timerFont
        self.cdLabel.place(x=1620, y=1025)

# Version Label
        self.versionLabel = Label(root, text="V " + self.versionNumber, fg="white", bg=self.rootColor)
        self.versionLabel['font'] = self.versionFont
        self.versionLabel.place(x=1842, y=1055)



        print("Broke out of loop")
        self.countdown(300)


root = Tk()
root.configure(background="gray10")
root.attributes('-fullscreen', True)
root.resizable(False, False)
root.geometry("1920x1080")
app = Window(root)
root.mainloop()
