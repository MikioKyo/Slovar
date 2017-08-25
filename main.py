﻿# import the library
from appJar import gui
from os import listdir
 
 
# grid tip
# "row=1 column=2 colspan=1 rowspan=2", 1, 2, 1, 2)
 
# handle button events
def press(button):
    if button == "Cancel" or button == "Выход":
        app.stop()
    elif button == "Выбрать":
        name = app.getListItems("list")[0]
        app.setLabel("header", name[:-4])
        otv=open(list).readlines().splitlines(";")
        app.setLabel("main_phrase", otv)
    else:
        usr = "123"
        pwd = app.getEntry("Password")
        print("User:", usr, "Pass:", pwd)
 
# create a GUI variable called app
app = gui("Dictionary fiesta", "1280x550")
app.setFont(18)
app.setResizable(canResize=False)
app.setStretch("both")
 
# Name of the current file being processed
app.addLabel("header", "Общий диктант на разные правила", row=0, column=0, colspan=2)
 
# Left column with files list and exit buttons
app.startPanedFrame("select_window", row=1, column=0)

files = listdir("./slbase")
mytxt = list(filter(lambda x: x.endswith('.txt'), files))

app.addListBox("list", mytxt, 1,2,1,2)
app.addButtons(["Выбрать", "Выход"], press, row=3, column=2)
app.stopPanedFrame()
app.getListBoxWidget("list").config(width=1)
 
 
# Right column with main actions
app.startLabelFrame("main_window", row=1, column=1)
app.addLabel("main_phrase", "без_дейный")
app.getLabelWidget("main_phrase").config(font="Times 30", width=30)
 
# variants buttons
app.startPanedFrame("p1")
app.addButtons(["ы", "и"], press)
app.stopPanedFrame()
 
app.setLabelSticky("main_phrase", "wns")
app.setPanedFrameSticky("p1", "ew")
app.stopLabelFrame()
 
app.setPanedFrameSticky("select_window", "nsw")
app.setLabelFrameSticky("main_window", "nsew")
 
# start the GUI
app.go()