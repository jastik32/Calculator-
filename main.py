import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QThread, QObject
from PyQt5.QtGui import QPalette, QFont
from PyQt5.QtWidgets import QTableWidgetItem
from calc import *

#Сделать кнопки кликабельными по своему назначению
#Сделать взаимодействие между кнопками
#


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda: self.add_data_to_textbox(self.ui.pushButton.text()))
        self.ui.pushButton_2.clicked.connect(lambda: self.add_data_to_textbox(self.ui.pushButton_2.text()))
        self.ui.pushButton_3.clicked.connect(lambda: self.add_data_to_textbox(self.ui.pushButton_3.text()))
        self.ui.pushButton_4.clicked.connect(lambda: self.add_data_to_textbox(self.ui.pushButton_4.text()))
        self.ui.pushButton_5.clicked.connect(lambda: self.add_data_to_textbox(self.ui.pushButton_5.text()))
        self.ui.pushButton_6.clicked.connect(lambda: self.add_data_to_textbox(self.ui.pushButton_6.text()))
        self.ui.pushButton_7.clicked.connect(lambda: self.add_data_to_textbox(self.ui.pushButton_7.text()))
        self.ui.pushButton_8.clicked.connect(lambda: self.add_data_to_textbox(self.ui.pushButton_8.text()))
        self.ui.pushButton_9.clicked.connect(lambda: self.add_data_to_textbox(self.ui.pushButton_9.text()))
        self.ui.pushButton_10.clicked.connect(lambda: self.add_data_to_textbox(self.ui.pushButton_10.text()))
        self.ui.pushButton_11.clicked.connect(lambda: self.add_data_to_textbox(self.ui.pushButton_11.text()))
        self.ui.pushButton_12.clicked.connect(lambda: self.add_data_to_textbox(self.ui.pushButton_12.text()))
        self.ui.pushButton_13.clicked.connect(lambda: self.add_data_to_textbox(self.ui.pushButton_13.text()))
        self.ui.pushButton_14.clicked.connect(lambda: self.add_data_to_textbox(self.ui.pushButton_14.text()))
        self.ui.pushButton_15.clicked.connect(self.clear_result)
        self.ui.pushButton_16.clicked.connect(self.get_result)
        self.ui.pushButton_17.clicked.connect(lambda: self.add_data_to_textbox(self.ui.pushButton_17.text()))
        self.ui.pushButton_18.clicked.connect(lambda: self.add_data_to_textbox(self.ui.pushButton_18.text()))
        self.ui.pushButton_19.clicked.connect(lambda: self.add_data_to_textbox(self.ui.pushButton_19.text()))




    def add_data_to_textbox(self, data: str):
        self.ui.textEdit.insertPlainText(data)


    def get_result(self, data: int):
        if self.check_correct_textbox():
            return
        try:
            correct_data = eval(self.ui.textEdit.toPlainText())
            self.ui.textEdit.insertPlainText(f'={correct_data}')

        except Exception as E:
            self.ui.textEdit.append("Ошибка!")

    def clear_result(self):
        self.ui.textEdit.clear()


    def check_correct_textbox(self):
        return '=' in self.ui.textEdit.toPlainText()









if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())