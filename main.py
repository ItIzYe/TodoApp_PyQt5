import json
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Fenster(QWidget):
    def __init__(self):
        super(Fenster, self).__init__()

        self.menue()
    def menue(self):
        file = 'todos.json'
        self.biglabel = QLabel(self)
        self.biglabel.setText("TODO APP")
        self.biglabel.setStyleSheet("QLabel{height: 100px; width: 1080px; align-text: center; "
                                    "background-color: #121212; color: white;}")
        self.biglabel.resize(1920, 1080)
        self.biglabel.setAlignment(Qt.AlignHCenter)
        self.biglabel.setFont(QtGui.QFont('Bahnschrift', 40, QtGui.QFont.Bold))
        self.biglabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


        self.wodo = QLineEdit(self)
        self.wodo.setStyleSheet("border-radius: 50px; align-items: center;")
        self.wodo.setPlaceholderText("Add Todo name...")
        self.wodo.setFont(QtGui.QFont('Bahnschrift', 20, QtGui.QFont.Bold))
        self.wodo.move(840, 200)

        self.wesc = QLineEdit(self)
        self.wesc.setStyleSheet("border-radius: 50px; align-items: center;")
        self.wesc.setPlaceholderText("Add description...")
        self.wesc.setFont(QtGui.QFont('Bahnschrift', 20, QtGui.QFont.Bold))
        self.wesc.move(840, 300)

        self.wimer = QLineEdit(self)
        self.wimer.setStyleSheet("border-radius: 50px; align-items: center;")
        self.wimer.setPlaceholderText("Add Timer...")
        self.wimer.setFont(QtGui.QFont('Bahnschrift', 20, QtGui.QFont.Bold))
        self.wimer.move(840, 400)


        self.wabel = QLineEdit(self)
        self.wabel.setStyleSheet("border-radius: 50px; align-items: center;")
        self.wabel.setPlaceholderText("Add Label...")
        self.wabel.setFont(QtGui.QFont('Bahnschrift', 20, QtGui.QFont.Bold))
        self.wabel.move(840, 500)

        self.button = QPushButton(self)
        self.button.move(840, 650)
        self.button.resize(100, 25)
        #button.setStyleSheet("button{border-radius: 20px}")
        #self.button.setGeometry(100, 100, 65, 35)
        self.button.clicked.connect(self.clicked_todo)
        self.button.clicked.connect(self.clicked_desc)
        self.button.clicked.connect(self.clicked_timer)
        self.button.clicked.connect(self.clicked_label)

        self.button.clicked.connect(self.save_todos)

        #yn = input("print?")
        #if yn.lower() == "y":
        #    for key in data['todos']['label']['work']:
        #        print(key)


        self.setWindowTitle("")
        self.setWindowIcon(QIcon("img/r.png"))
        self.showMaximized()

    def clicked_todo(self, text):
        print(self.wodo.text())
        self.todo_a = self.wodo.text()

    def clicked_desc(self, text):
        print(self.wesc.text())
        self.desc_a = self.wesc.text()

    def clicked_timer(self, text):
        print(self.wimer.text())
        self.timer_a = self.wimer.text()

    def clicked_label(self, text):
        print(self.wabel.text())
        self.label_a = self.wabel.text()


    def save_todos (self):
        print("check")
        if self.label_a.lower() == 'work':
            print("test1 comp")
            self.file = open("todos.json", 'r')
            self.data = json.load(self.file)
            self.todo_a.close()
            self.file = open("todos.json", 'w')
            self.list = {self.todo_a: {"description": self.desc_a,
                                        "timer": self.timer_a}}
            print("check")
            self.data['todos']['label']['work'].update(list)
            json.dump(self.data, self.file, indent=4)
            self.file.close()

        if self.wabel.text().lower() == 'edu':
            print("test2 comp")
            file = open(file, 'r')
            data = json.load(file)
            file.close()
            file = open("todos.json", 'w')
            list = {self.wodo.text(): {"description": self.wesc.text(),
                           "timer": self.wimer.text()}}

            data['todos']['label']['edu'].update(list)
            json.dump(data, file, indent=4)
            file.close()

        if self.wabel.text().lower() == 'personal':
            print("test3 comp")
            file = open(file, 'r')
            data = json.load(file)
            file.close()
            file = open("todos.json", 'w')
            list = {self.wodo.text(): {"description": self.wesc.text(),
                           "timer": self.wimer.text()}}

            data['todos']['label']['personal'].update(list)
            json.dump(data, file, indent=4)
            file.close()


app = QApplication(sys.argv)

w = Fenster()
w.show()

sys.exit(app.exec_())


