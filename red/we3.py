# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'we3.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets  
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(638, 491)
        MainWindow.setStyleSheet("rgb255, 172, 254")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 290, 191, 191))
        #pixmap = QPixmap('CaptureF.PNG')
        self.pushButton_4.setStyleSheet("background-image: url(shutdown (2).png);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        #msg.setText("This is the main text!")
        #x = msg.exec_()  # this will show our messagebox
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 210, 581, 41))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, -10, 121, 71))
        self.label.setStyleSheet("background-image: url(CaptureF.PNG);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalScrollBar_2 = QtWidgets.QScrollBar(self.groupBox_2)
        self.horizontalScrollBar_2.setGeometry(QtCore.QRect(130, -10, 241, 71))
        self.horizontalScrollBar_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.horizontalScrollBar_2.setMaximum(1)
        self.horizontalScrollBar_2.setPageStep(1)
        self.horizontalScrollBar_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_2.setObjectName("horizontalScrollBar_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(380, -20, 121, 71))
        self.label_2.setStyleSheet("background-image: url(F.PNG);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(200, 0, 251, 191))
        self.pushButton.setStyleSheet(" \n""border-image: url(th (3).jfif);")

        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(100, 190, 120, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(315, 290, 231, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 60, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/th (2).jfif\"/></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        
def clickMethod(self):
        QMessageBox.about(self, "Title", "Message")
 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())