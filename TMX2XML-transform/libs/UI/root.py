# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:/Workspace/Python-workspace/TMX2XML-transform/libs/UI/root.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(344, 322)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 321, 301))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(0, 230, 321, 30))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_4.setStyleSheet("border: 1px solid green;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pbar1 = QtWidgets.QProgressBar(self.frame_4)
        self.pbar1.setGeometry(QtCore.QRect(5, 3, 311, 23))
        self.pbar1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pbar1.setStyleSheet("border-style: none;\n"
"color: red;")
        self.pbar1.setProperty("value", 0)
        self.pbar1.setAlignment(QtCore.Qt.AlignCenter)
        self.pbar1.setObjectName("pbar1")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(0, 270, 321, 31))
        self.frame_5.setStyleSheet("border: 1px solid green;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.lb2 = QtWidgets.QLabel(self.frame_5)
        self.lb2.setGeometry(QtCore.QRect(0, 5, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.lb2.setFont(font)
        self.lb2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lb2.setStyleSheet("border-style: none;")
        self.lb2.setLineWidth(0)
        self.lb2.setText("")
        self.lb2.setAlignment(QtCore.Qt.AlignCenter)
        self.lb2.setObjectName("lb2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(1, 1, 319, 111))
        self.frame_2.setStyleSheet("border: 1px solid green;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.cb1 = QtWidgets.QComboBox(self.frame_2)
        self.cb1.setGeometry(QtCore.QRect(10, 40, 121, 22))
        self.cb1.setObjectName("cb1")
        self.bt1 = QtWidgets.QPushButton(self.frame_2)
        self.bt1.setGeometry(QtCore.QRect(233, 20, 75, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt1.setFont(font)
        self.bt1.setObjectName("bt1")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(1, 121, 319, 101))
        self.frame_3.setStyleSheet("border: 1px solid green;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.le1 = QtWidgets.QLineEdit(self.frame_3)
        self.le1.setGeometry(QtCore.QRect(10, 38, 301, 20))
        self.le1.setObjectName("le1")
        self.bt2 = QtWidgets.QPushButton(self.frame_3)
        self.bt2.setGeometry(QtCore.QRect(234, 66, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bt2.setFont(font)
        self.bt2.setObjectName("bt2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "파트 선택"))
        self.bt1.setText(_translate("MainWindow", "실행"))
        self.label_3.setText(_translate("MainWindow", "TMX 폴더 선택"))
        self.bt2.setText(_translate("MainWindow", "폴더 선택"))
