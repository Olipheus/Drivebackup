# -*- coding: UTF-8 -*-
import tkinter
import _tkinter
import distutils
from distutils import dir_util 
from tkinter import *
import win32api
import sys
import subprocess
import os, string, datetime, time


today = datetime.date.today()

todaystr = today.isoformat()


#List of available devices

available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
forbiddendevices = ['C:', 'P:']
available_drives.insert(0, "Välj enhet att säkerhetskopiera")
available_drives = [x for x in available_drives if x not in forbiddendevices]

#specifying the save to and open folder


folder = "//pifil01/apps/Backup maskiner/"
folderopen = "\\\\pifil01\\apps\\Backup maskiner\\"



    
#list of machine will be part of folder name for backup


listofmachines = ["102", "103", "133", "134", "135", "138",
                  "139", "140", "141", "142", "147", "149",
                  "150", "151", "152", "153", "154", "156",
                  "157", "158", "159", "160", "161", "162",
                  "163", "164", "166", "167", "170", "171",
                  "172", "173", "227", "228", "229", "230",
                  "231", "236", "237", "243", "248", "255",
                  "265", "268", "269"]

#saving file function for variable folder naming

def savefiles():
    os.mkdir(folder + "Msk" + machinelist.get() + " " + todaystr)
    distutils.dir_util.copy_tree(devicelist.get(), folder + "Msk" + machinelist.get() + " " + todaystr)
    subprocess.Popen(['explorer',folderopen])            

def restart_script():
    python = sys.executable
    os.execl(python, python, * sys.argv)


#user interface

mainframe = Tk()

mainframe.geometry('{}x{}'.format(300, 250))
mainframe.title('Backup maskinprogram')

labelheader = Label(mainframe, text = 'Skapa backup av USB minne')
labelheader.pack()

devicelist = StringVar(mainframe)
devicelist.set("Välj enhet att säkerhetskopiera") # initial value

optiondevicelist = OptionMenu(mainframe, devicelist, *available_drives)

machinelist = StringVar (mainframe)
machinelist.set("Välj maskin")

optionmachinelist = OptionMenu(mainframe, machinelist, *listofmachines)



button1 = Button(mainframe, text = 'OK', command = savefiles, height = 2, width = 10)
button2 = Button(mainframe, wraplength = 100, text = 'Tryck här om USB sattes i efter programstart', command = restart_script, height = 4, width = 15)

#the order of the graphic elements

button2.pack()
optiondevicelist.pack()
optionmachinelist.pack()
button1.pack()

mainloop()
