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
# 1) Make program object oriented
# 2) Sort by priority --> date
# 3) Change date format to MM-DD-YYYY
# 4) Create an authorization function, no need to reauthorize every 5 mins



class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()


    def init_window(self):
        
        for widget in root.winfo_children():
                widget.destroy()

        self.master.title("IT Department Open Tickets")

        headerFont = font.Font(size=18, family='Helvetica', weight='bold')
        displayNameFont = font.Font(size=15, family='Times New Roman', weight='bold')
        valueFont = font.Font(size=15, family='Times New Roman')
        valueFont2 = font.Font(size=13, family='Times New Roman')



        mydata = {
          "grant_type": "password",
          "username": "SYSTEM ADMINISTRATION\WEBAPI",
          "password": "AA7Aj80"
        }
        token = requests.get("http://10.0.6.8/TrackIt/WebApi/token", data=mydata)

        bearerToken = token.json()["access_token"]

        myHeader = {
          "Authorization": "Bearer " + bearerToken
        }

        print("Screen Refreshed")
        rcounter = 0
        ccounter = 0
        for i in range(300, 800):

            url = 'http://10.0.6.8/TrackIt/WebApi/tickets/' + str(i)
            response = requests.get(url, headers=myHeader)

            if response:
                ticket = response.json()
                if ticket["Ticket"]["96"]["Value"] == "Open":

                    try:
                        tID = ticket["Ticket"]["1"]["Value"]
                    except:
                        #print("Cannot find ticket ID")
                        tID = "N/A"

                    try:
                        tOpen = str(ticket["Ticket"]["12"]["Value"])[:10]
                    except:
                        #print("Cannot find ticket Open Time")
                        tOpen = "N/A"

                    try:
                        tSummary = ticket["Ticket"]["22"]["Value"]
                    except:
                        #print("Cannot find ticket Summary")
                        tSummary = "N/A"

                    try:
                        tAddInfo = ticket["Ticket"]["7"]["Value"]
                    except:
                        #print("Cannot find ticket Additional Info")
                        tAddInfo = "N/A"

                    try:
                        tCategory = ticket["Ticket"]["72"]["Value"]
                    except:
                        #print("Cannot find ticket Category")
                        tCategory = "N/A"

                    try:
                        tPriority = str(ticket["Ticket"]["107"]["Value"])[0]
                    except:
                        #print("Cannot find ticket Priority")
                        tPriority = ""

                    try:
                        tStatus = ticket["Ticket"]["96"]["Value"]
                    except:
                        #print("Cannot find ticket Status")
                        tStatus = "N/A"

                    try:
                        tRequestor= ticket["Ticket"]["149"]["Value"]
                    except:
                        #print("Cannot find ticket Requestor")
                        tRequestor = "N/A"

                    try:
                        tOpenedBy = ticket["Ticket"]["177"]["Value"]
                    except:
                        #print("Cannot find ticket OpenedBy")
                        tOpenedBy = "N/A"

                    try:
                        tAssigned = ticket["Ticket"]["157"]["Value"]
                    except:
                        #print("Cannot find ticket Assigned")
                        tAssigned = "N/A"



                    color = "skyblue1"


                    if tPriority == "1":
                        pcolor = "red3"
                    elif tPriority == "2":
                        pcolor = "darkorange2"
                    elif tPriority == "3":
                        pcolor= "yellow2"
                    elif tPriority == "4":
                        pcolor= "deepskyblue2"
                    elif tPriority == "5":
                        pcolor= color
                    else:
                        pcolor = color






                    frame1 = Frame(root,bg=color,width=374,height=354,padx=3,pady=3)
                    frame1.grid(row=rcounter, column=ccounter, padx=5,pady=3)




            # Ticket ID Label
                    label = Label(frame1, text="Ticket " + str(tID),bg=color)
                    label['font'] = headerFont
                    label.place(x=105,y=1)


            # Priority Label
                    label0 = Label(frame1, text= str(tPriority), bg=pcolor)
                    label0['font'] = headerFont
                    label0.place(x=5,y=1)


            # Date Label
                    label2 = Label(frame1, text="Opened:", wraplength= 250,bg=color)
                    label2['font'] = valueFont2
                    label2.place(x=272,y=1)

                    label0 = Label(frame1, text= str(tOpen), bg=color)
                    label0['font'] = displayNameFont
                    label0.place(x=265,y=20)




            # Category Label
                    label1 = Label(frame1, text="Category: ",bg=color)
                    label1['font'] = displayNameFont
                    label1.place(x=7,y=46)

                    label2 = Label(frame1, text=str(tCategory), wraplength= 250,bg=color)
                    label2['font'] = valueFont
                    label2.place(x=115,y=46)


            # Summary Label
                    label1 = Label(frame1, text="Summary: ",bg=color)
                    label1['font'] = displayNameFont
                    label1.place(x=7,y=72)

                    label2 = Label(frame1, text=str(tSummary), wraplength= 250,bg=color, justify="left")
                    label2['font'] = valueFont
                    label2.place(x=115,y=72)


            # Requestor Label
                    label1 = Label(frame1, text="Requested by: ",bg=color)
                    label1['font'] = displayNameFont
                    label1.place(x=7,y=155)

                    label2 = Label(frame1, text=str(tRequestor), wraplength= 200,bg=color)
                    label2.place(x=140,y=155)
                    label2['font'] = valueFont


            # Opened Label
                    label1 = Label(frame1, text="Opened by: ",bg=color)
                    label1['font'] = displayNameFont
                    label1.place(x=7,y=180)

                    label2 = Label(frame1, text=str(tOpenedBy), wraplength= 200,bg=color)
                    label2.place(x=140,y=180)
                    label2['font'] = valueFont


            # Assigned Label
                    label1 = Label(frame1, text="Assigned to: ",bg=color)
                    label1['font'] = displayNameFont
                    label1.place(x=7,y=205)

                    label2 = Label(frame1, text=str(tAssigned), wraplength= 200,bg=color)
                    label2.place(x=140,y=205)
                    label2['font'] = valueFont


            # Info Label
                    label1 = Label(frame1, text="Additional Info: ",bg=color)
                    label1['font'] = displayNameFont
                    label1.place(x=7,y=235)

                    label2 = Label(frame1, text=str(tAddInfo), wraplength= 340,bg=color, justify="left")
                    label2.place(x=20,y=260)
                    label2['font'] = valueFont

                    rcounter += 1
                    if rcounter > 2:
                        ccounter +=1
                        rcounter = 0





        print("Broke out of loop")
        root.after(300000, self.init_window)
        # frame2 = Frame(root,bg="red",width=375,height=255)
        # frame2.pack(padx=5,pady=3, anchor="nw", side="top")
        #
        # frame2 = Frame(root,bg="red",width=375,height=255)
        # frame2.pack(padx=5,pady=3, anchor="nw", side="top")
        #
        # frame2 = Frame(root,bg="red",width=375,height=255)
        # frame2.pack(padx=5,pady=3, anchor="nw", side="top")










root = Tk()
root.configure(background="gray20")
root.attributes('-fullscreen', True)
root.resizable(False, False)
root.geometry("1920x1080")
app = Window(root)
root.mainloop()
