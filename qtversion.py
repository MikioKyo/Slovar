# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_slovar.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QButtonGroup
import sys
from os import listdir
import random

lineNumber = 1
rightAnswer = ""
rightAnswerCount = 0
wrongAnswerCount = 0
name = ""
exerciseLines = []

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(717, 541)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 701, 491))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.excerciseTitle = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.excerciseTitle.setMinimumSize(QtCore.QSize(0, 50))
        self.excerciseTitle.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.excerciseTitle.setFont(font)
        self.excerciseTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.excerciseTitle.setObjectName("excerciseTitle")
        self.verticalLayout.addWidget(self.excerciseTitle)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.testFilesListWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.testFilesListWidget.setMaximumSize(QtCore.QSize(150, 16777215))
        self.testFilesListWidget.setObjectName("testFilesListWidget")
        files = listdir("./")
        mytxt = list(filter(lambda x: x.endswith('.txt'), files))
        for i in mytxt:
            item = QtWidgets.QListWidgetItem(i)
            self.testFilesListWidget.addItem(item)

        self.verticalLayout_2.addWidget(self.testFilesListWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.selectButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.selectButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.selectButton.setObjectName("selectButton")
        self.selectButton.clicked.connect(self.selectExercise)

        self.horizontalLayout_3.addWidget(self.selectButton)
        self.exitButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exitButton.setMaximumSize(QtCore.QSize(70, 16777215))
        self.exitButton.setObjectName("exitButton")
        self.exitButton.clicked.connect(QCoreApplication.instance().quit)
        self.horizontalLayout_3.addWidget(self.exitButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setMinimumSize(QtCore.QSize(500, 0))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 481, 411))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(8)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.excerciseQuestionLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.excerciseQuestionLabel.setFont(font)
        self.excerciseQuestionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.excerciseQuestionLabel.setObjectName("excerciseQuestionLabel")
        self.verticalLayout_4.addWidget(self.excerciseQuestionLabel)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.answerButtonOne = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.answerButtonOne.setObjectName("answerButtonOne")
        self.horizontalLayout_4.addWidget(self.answerButtonOne)
        self.answerButtonTwo = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.answerButtonTwo.setObjectName("answerButtonTwo")
        self.horizontalLayout_4.addWidget(self.answerButtonTwo)
        self.answerButtonGroup = QButtonGroup()
        self.answerButtonGroup.addButton(self.answerButtonOne)
        self.answerButtonGroup.addButton(self.answerButtonTwo)
        self.answerButtonGroup.buttonClicked.connect(self.selectAnswer)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayoutWidget.raise_()
        self.excerciseQuestionLabel.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 717, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.excerciseTitle.setText(_translate("MainWindow", "Безударные Гласные 1"))
        self.selectButton.setText(_translate("MainWindow", "Выбрать"))
        self.exitButton.setText(_translate("MainWindow", "Выход"))
        self.excerciseQuestionLabel.setText(_translate("MainWindow", "Зав_вать локоны"))
        self.answerButtonOne.setText(_translate("MainWindow", "И"))
        self.answerButtonTwo.setText(_translate("MainWindow", "Е"))

    def selectExercise(self):
        global name
        global exerciseLines
        global rightAnswer

        exerciseHeader = ""
        name = self.testFilesListWidget.selectedIndexes()[0].data()
        with open(name, 'r', encoding='utf-8') as exerciseFile:
            exerciseHeader = exerciseFile.readline()
            exerciseLines = exerciseFile.readlines()
        print(exerciseHeader)
        exercise = exerciseLines[0] 
        exerciseQuestion = exercise.split(";")[0].strip()
        exerciseAnswerOne = exercise.split(";")[1].strip()
        exerciseAnswerTwo = exercise.split(";")[2].strip()
        rightAnswer = exercise.split(";")[3].strip()


        self.excerciseTitle.setText(exerciseHeader)
        self.excerciseQuestionLabel.setText(exerciseQuestion)

        self.answerButtonOne.setText(exerciseAnswerOne)
        self.answerButtonTwo.setText(exerciseAnswerTwo)
        
    def selectAnswer(self, answerButtonGroup):
        global lineNumber
        global rightAnswer
        global exerciseLines
        global rightAnswerCount
        global wrongAnswerCount

        button_clicked = self.answerButtonGroup.checkedButton()
        print("Right answer: "+rightAnswer, "Your answer: "+button_clicked.text())
        if button_clicked.text() == rightAnswer:
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
        self.excerciseQuestionLabel.setText(exerciseQuestion)
        self.answerButtonOne.setText(exerciseAnswerOne)
        self.answerButtonTwo.setText(exerciseAnswerTwo)

        lineNumber = lineNumber + 1
        print(lineNumber, len(exerciseLines))

        if lineNumber == len(exerciseLines):
            print("Test")
            app.infoBox("Результаты", "Правильных: {} \n Неправильных: {}".format(rightAnswerCount, wrongAnswerCount))


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)

    window.show()
    sys.exit(app.exec_())