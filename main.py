# import the library
from appJar import gui
from os import listdir
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
 
# grid tip
# "row=1 column=2 colspan=1 rowspan=2", 1, 2, 1, 2)
# handle button events
line = 0

def press(button):
    global line
    if button == "Cancel" or button == "Выход":
        app.stop()
    elif button == "Выбрать":
        name = app.getListItems("list")[line]
        app.setLabel("header", name[:-4])
        otv=open(name).readlines()[0].split(";")
        app.setLabel("main_phrase", otv[0])
        app.setButton("ы", otv[1])
        app.setButton("и", otv[2])
        
    elif button == "ы" or button == "и":
        name = app.getListItems("list")[0]
        otv=open(name).readlines()[line].split(";")
        app.setLabel("main_phrase", otv[0])
        app.setButton("ы", otv[1])
        app.setButton("и", otv[2])
        line = line + 1
        print(line, len(name))
        if line == len(name):
            a = 1
            b = 2
            print("Test")
            app.infoBox("Результаты", "Правильных: {} \n Неправильных: {}".format(a, b))
    else:
        pass
 
# create a GUI variable called app
app = gui("Dictionary fiesta", "1280x550")
app.setFont(18)
app.setResizable(canResize=False)
app.setStretch("both")
 
# Name of the current file being processed
app.addLabel("header", "Общий диктант на разные правила", row=0, column=0, colspan=2)
 
# Left column with files list and exit buttons
app.startPanedFrame("select_window", row=1, column=0)

files = listdir("./")
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