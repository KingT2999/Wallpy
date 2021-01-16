# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Vahram\Desktop\Python\wallpy\wallpy.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(394, 264)
        Dialog.setWindowOpacity(0.9)
        Dialog.setStyleSheet("QDialog{\n"
"    background-color: grey;\n"
"}")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 341, 41))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    border: 2.5px solid lightblue;\n"
"    border-radius:15px;\n"
"    background-color: rgb(221, 221, 221);\n"
"    color: rgb(170, 170, 255);\n"
"    font: 12pt \"Meiryo UI\";\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 10, 251, 21))
        self.label.setStyleSheet("QLabel{\n"
"    font: 15pt \"Arial\";\n"
"    color: rgb(255, 128, 0);\n"
"}")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 110, 341, 91))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    font: 12pt \"Metro\";\n"
"    color: cyan;\n"
"    background-color: #bfbfbf;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #6b6b6b;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(20, 220, 151, 17))
        self.checkBox.setStyleSheet("QCheckBox{\n"
"    font: 75 14pt \"Lithograph\";\n"
"    color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 85, 255, 255), stop:1 rgba(195, 42, 255, 255));\n"
"}")
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "WallPy"))
        self.label.setText(_translate("Dialog", "Напишите название файла"))
        self.pushButton.setText(_translate("Dialog", "SetWallaper"))
        self.checkBox.setText(_translate("Dialog", "NO AUDIO"))


if __name__ == "__main__":
    import sys, os

    app = QtWidgets.QApplication(sys.argv)

    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

    def bp():
    	os.system("wp id >id.txt")
    	file = open('id.txt')
    	if ui.lineEdit.text() == "":
    		ui.label.setText("Введите текст")
    	else:
	    	os.system("wp run mpv --wid=" + file.read() + " video/" + ui.lineEdit.text() + " --loop=inf --player-operation-mode=pseudo-gui --force-window=yes --no-audio")
	    	file.close()
    ui.pushButton.clicked.connect(bp)
    
    sys.exit(app.exec_())