# import the library
from appJar import gui
from os import listdir
 
# grid tip
# "row=1 column=2 colspan=1 rowspan=2", 1, 2, 1, 2)
# handle button events
lineNumber = 1
rightAnswerCount = 0
wrongAnswerCount = 0
name = ""
# otv = []
exerciseHeader = ""
exerciseLines = []
def selectExercise(button):
    global name
    global otv
    global exerciseHeader
    global exerciseLines
    name = app.getListItems("list")[0]
    app.setLabel("header", name[:-4])
    # otv=open(name, 'r', encoding='utf-8').readlines()[0].split(";")
    with open(name, 'r', encoding='utf-8') as exerciseFile:
     #   lines = exerciseFile.readlines()
        exerciseHeader = exerciseFile.readline()
        exerciseLines = exerciseFile.readlines()
    app.setLabel("header", exerciseHeader)
def exercise(button):
    global lineNumber
    global rightAnswer
    global wrongAnswer
    global exerciseHeader
    global exerciseLines
    global rightAnswerCount
    global wrongAnswerCount
    
    if button == "Выбрать":
        print(open(name, 'r', encoding='utf-8').readlines()[0])
        app.setLabel("main_phrase", exerciseHeader)
        app.setButton("ы", exerciseAnswerOne[1]) 	
        app.setButton("и", exerciseAnswerTwo[2])
    elif button == "ы" or button == "и":
       # print(exerciseLines)
        exercise = exerciseLines[lineNumber]
        exerciseQuestion = exercise.split(";")[0]
        exerciseAnswerOne = exercise.split(";")[1]
        exerciseAnswerTwo = exercise.split(";")[2]
        exerciseRightAnswer = exercise.split(";")[3]
        app.setLabel("main_phrase", exerciseQuestion)
        app.setButton("ы", exerciseAnswerOne)
        app.setButton("и", exerciseAnswerTwo)
        lineNumber = lineNumber + 1
        print(lineNumber, len(exerciseLines))

        if answerButton1 == exerciseRightAnswer:
            rightAnswerCount = rightAnswerCount + 1
        else:
            wrongAnswerCount = wrongAnswerCount + 1

        if lineNumber == len(exerciseLines):
            print("Test")
            app.infoBox("Результаты", "Правильных: {} \n Неправильных: {}".format(rightAnswerCount, wrongAnswerCount))
    else:
        pass
def press(button):
    app.stop()
 
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

app.addListBox("list", mytxt, 1,2,2,2)
#app.addButton(["Выбрать", "Выход"], press, row=3, column=2)
app.addButton("Выбрать", selectExercise, row=3, column=2)
app.addButton("Выход", press, row=3, column=3)
app.stopPanedFrame()
app.getListBoxWidget("list").config(width=1)
 
 
# Right column with main actions
app.startLabelFrame("main_window", row=1, column=1)
app.addLabel("main_phrase", "без_дейный")
app.getLabelWidget("main_phrase").config(font="Times 30", width=30)
 
# variants buttons
app.startPanedFrame("p1")

answerButton1 = exerciseAnswerOne
answerButton2 = exerciseAnswerTwo

app.addButtons([answerButton1, answerButton2], exercise)
app.stopPanedFrame()
 
 
 
app.setLabelSticky("main_phrase", "wns")
app.setPanedFrameSticky("p1", "ew")
app.stopLabelFrame()
 
app.setPanedFrameSticky("select_window", "nsw")
app.setLabelFrameSticky("main_window", "nsew")
 
# start the GUI
app.go()