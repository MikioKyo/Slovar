# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from appJar import gui
from os import listdir
import random

# grid tip
# "row=1 column=2 colspan=1 rowspan=2", 1, 2, 1, 2)
# handle button events
lineNumber = 1
rightAnswer = ""
rightAnswerCount = 0
wrongAnswerCount = 0
name = ""
# otv = []
exerciseLines = []


def selectExercise(button):
    global name
    global otv
    global exerciseLines
    global rightAnswer

    exerciseHeader = ""
    name = app.getListItems("list")[0]
    with open(name, 'r', encoding='utf-8') as exerciseFile:
        exerciseHeader = exerciseFile.readline()
        exerciseLines = exerciseFile.readlines()
    print(exerciseHeader)
    exercise = exerciseLines[0]
    exerciseQuestion = exercise.split(";")[0].strip()
    exerciseAnswerOne = exercise.split(";")[1].strip()
    exerciseAnswerTwo = exercise.split(";")[2].strip()
    rightAnswer = exercise.split(";")[3].strip()


    app.setLabel("header", exerciseHeader)
    app.setLabel("main_phrase", exerciseQuestion)

    app.setButton("first_answer_button", exerciseAnswerOne)
    app.setButton("second_answer_button", exerciseAnswerTwo)


def exercise(button):
    global lineNumber
    global rightAnswer
    global exerciseLines
    global rightAnswerCount
    global wrongAnswerCount

    button_clicked = app.getButtonWidget(button)['text']

    print("Right answer: "+rightAnswer, "Your answer: "+button_clicked)
    if button_clicked == rightAnswer:
        print("Right!")
        rightAnswerCount = rightAnswerCount + 1
    else:
        print("Wrong(")
        wrongAnswerCount = wrongAnswerCount + 1

    questionShuffle = [1, 2]
    exercise = exerciseLines[lineNumber]
    exerciseQuestion = exercise.split(";")[0].strip()
    x = random.choice(questionShuffle)
    exerciseAnswerOne = exercise.split(";")[x].strip()
    questionShuffle.remove(x)
    exerciseAnswerTwo = exercise.split(";")[random.choice(questionShuffle)].strip()
    rightAnswer = exercise.split(";")[3].strip()
    app.setLabel("main_phrase", exerciseQuestion)
    app.setButton("first_answer_button", exerciseAnswerOne)
    app.setButton("second_answer_button", exerciseAnswerTwo)

    lineNumber = lineNumber + 1
    print(lineNumber, len(exerciseLines))

    if lineNumber == len(exerciseLines):
        print("Test")
        app.infoBox("Результаты", "Правильных: {} \n Неправильных: {}".format(rightAnswerCount, wrongAnswerCount))


def press(button):
    app.stop()
 
# create a GUI variable called app
app = gui("Dictionary fiesta", "900x550")
app.setFont(18)
app.setResizable(canResize=False)
app.setStretch("both")
 
# Name of the current file being processed
app.addLabel("header", "Общий диктант на разные правила", row=0, column=0, colspan=2)
 
# Left column with files list and exit buttons
app.startPanedFrame("select_window", row=1, column=0)

files = listdir("./")
mytxt = list(filter(lambda x: x.endswith('.txt'), files))

app.addListBox("list", mytxt, 1,2,2,2)
#app.addButton(["Выбрать", "Выход"], press, row=3, column=2)
app.addButton("Выбрать", selectExercise, row=3, column=2)
app.addButton("Выход", press, row=3, column=3)
app.stopPanedFrame()
app.getListBoxWidget("list").config(width=2)
 
 
# Right column with main actions
app.startLabelFrame("main_window", row=1, column=1)
app.addLabel("main_phrase", "без_дейный")
app.getLabelWidget("main_phrase").config(font="Times 30", width=30)
 
# variants buttons
app.startPanedFrame("p1")

# app.addButtons(["1", "2"], exercise)
app.addNamedButton("", "first_answer_button", exercise, row=3, column=4)
app.addNamedButton("", "second_answer_button", exercise, row=3, column=5)
app.stopPanedFrame()
 
 
 
app.setLabelSticky("main_phrase", "wns")
app.setPanedFrameSticky("p1", "ew")
app.stopLabelFrame()
 
app.setPanedFrameSticky("select_window", "nsw")
app.setLabelFrameSticky("main_window", "nsew")
 
# start the GUI
app.go()