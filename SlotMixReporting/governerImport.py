# import os, os.path
# import win32com.client
#
# if os.path.exists("Governer.xls"):
#     xl=win32com.client.Dispatch("Excel.Application")
#     xl.Workbooks.Open(os.path.abspath("Governer.xls"))
#     xl.Application.Run("Governer.xls!Sheet1.Import_data")
#     #xl.Application.Save() # if you want to save then uncomment this line and change delete the ", ReadOnly=1" part from the open function.
#     #xl.Application.Quit() # Comment this out if your excel script closes
#     del xl

"""
 --- To Do:
     -- [DONE] Automate Import to Governer File
     -- [DONE] Automate Opening of CAD Drawing (autorun update.lsp on startup)
     -- Archive and renname/copy .dwg gile to an archive folder
     -- Archive Slot Mix Data
     -- Email out sorted slot machine data
     -- Create Historcial Data webserver

    IN CAD:
     -- Create serperate layers for tables (can be hidden)
     -- Outline Banks depending on color of table winnings
     -- Create master table on side of drawing that displays all table data

"""

#Import the following library to make use of the DispatchEx to run the macro
import win32com.client as wincl
import os,subprocess, platform

if os.path.exists("C:\\Users\\arose\\Programs\\SlotMixReporting\\backup\\the zip\\Governer.xls"):

    # DispatchEx is required in the newest versions of Python.
    excel_macro = wincl.DispatchEx("Excel.application")
    excel_path = os.path.expanduser("C:\\Users\\arose\\Programs\\SlotMixReporting\\backup\\the zip\\Governer.xls")
    workbook = excel_macro.Workbooks.Open(Filename = excel_path, ReadOnly =1)
    excel_macro.Application.Run("Sheet1.Import_data")
    #Save the results in case you have generated data
    workbook.Save()
    excel_macro.Application.Quit()
    del excel_macro


os.startfile("C:\\Users\\arose\\Programs\\SlotMixReporting\\backup\\the zip\\QCC 1192 Current_031914.dwg")
#exec(open("C:\\Users\\arose\\Programs\\SlotMixReporting\\backup\\the zip\\QCC 1192 Current_031914.dwg").read())
