# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\Workspace\Python-workspace\AIR_Html_Converter\libs/Ui\root.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(494, 298)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.wg2 = QtWidgets.QWidget(self.centralwidget)
        self.wg2.setGeometry(QtCore.QRect(9, 59, 471, 151))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.wg2.setFont(font)
        self.wg2.setStyleSheet("#wg2 {border: 1px solid #e63f30;}")
        self.wg2.setObjectName("wg2")
        self.cb1 = QtWidgets.QComboBox(self.wg2)
        self.cb1.setGeometry(QtCore.QRect(66, 20, 121, 25))
        self.cb1.setObjectName("cb1")
        self.pb2 = QtWidgets.QPushButton(self.wg2)
        self.pb2.setGeometry(QtCore.QRect(145, 110, 120, 35))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pb2.setFont(font)
        self.pb2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pb2.setObjectName("pb2")
        self.pb1 = QtWidgets.QPushButton(self.wg2)
        self.pb1.setGeometry(QtCore.QRect(351, 60, 110, 35))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pb1.setFont(font)
        self.pb1.setObjectName("pb1")
        self.lb2 = QtWidgets.QLabel(self.wg2)
        self.lb2.setGeometry(QtCore.QRect(10, 65, 41, 20))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb2.setFont(font)
        self.lb2.setObjectName("lb2")
        self.pb3 = QtWidgets.QPushButton(self.wg2)
        self.pb3.setGeometry(QtCore.QRect(274, 110, 90, 35))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pb3.setFont(font)
        self.pb3.setObjectName("pb3")
        self.groupBox = QtWidgets.QGroupBox(self.wg2)
        self.groupBox.setGeometry(QtCore.QRect(231, 12, 231, 35))
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.rb1 = QtWidgets.QRadioButton(self.groupBox)
        self.rb1.setGeometry(QtCore.QRect(107, 9, 51, 20))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.rb1.setFont(font)
        self.rb1.setObjectName("rb1")
        self.rb2 = QtWidgets.QRadioButton(self.groupBox)
        self.rb2.setGeometry(QtCore.QRect(164, 9, 50, 20))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.rb2.setFont(font)
        self.rb2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.rb2.setAutoFillBackground(False)
        self.rb2.setChecked(True)
        self.rb2.setObjectName("rb2")
        self.lb3 = QtWidgets.QLabel(self.groupBox)
        self.lb3.setGeometry(QtCore.QRect(10, 9, 91, 20))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb3.setFont(font)
        self.lb3.setObjectName("lb3")
        self.pb4 = QtWidgets.QPushButton(self.wg2)
        self.pb4.setGeometry(QtCore.QRect(371, 110, 90, 35))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pb4.setFont(font)
        self.pb4.setObjectName("pb4")
        self.le1 = QtWidgets.QLineEdit(self.wg2)
        self.le1.setGeometry(QtCore.QRect(64, 61, 261, 25))
        self.le1.setObjectName("le1")
        self.lb1 = QtWidgets.QLabel(self.wg2)
        self.lb1.setGeometry(QtCore.QRect(11, 20, 41, 20))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb1.setFont(font)
        self.lb1.setObjectName("lb1")
        self.le2 = QtWidgets.QLineEdit(self.wg2)
        self.le2.setGeometry(QtCore.QRect(64, 111, 71, 33))
        self.le2.setObjectName("le2")
        self.label = QtWidgets.QLabel(self.wg2)
        self.label.setGeometry(QtCore.QRect(10, 119, 41, 16))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.wg1 = QtWidgets.QWidget(self.centralwidget)
        self.wg1.setEnabled(True)
        self.wg1.setGeometry(QtCore.QRect(9, 9, 471, 47))
        self.wg1.setAutoFillBackground(False)
        self.wg1.setStyleSheet("#wg1 {\n"
"    border: 1px solid #e63f30;\n"
"}\n"
"")
        self.wg1.setObjectName("wg1")
        self.mainTitle = QtWidgets.QLabel(self.wg1)
        self.mainTitle.setGeometry(QtCore.QRect(9, 9, 453, 29))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.mainTitle.setFont(font)
        self.mainTitle.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.mainTitle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mainTitle.setFrameShadow(QtWidgets.QFrame.Plain)
        self.mainTitle.setLineWidth(1)
        self.mainTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.mainTitle.setObjectName("mainTitle")
        self.wg3 = QtWidgets.QWidget(self.centralwidget)
        self.wg3.setGeometry(QtCore.QRect(10, 216, 471, 61))
        self.wg3.setStyleSheet("#wg3 {border: 1px solid #e63f30;}")
        self.wg3.setObjectName("wg3")
        self.pbar1 = QtWidgets.QProgressBar(self.wg3)
        self.pbar1.setGeometry(QtCore.QRect(10, 10, 451, 23))
        self.pbar1.setProperty("value", 0)
        self.pbar1.setOrientation(QtCore.Qt.Horizontal)
        self.pbar1.setObjectName("pbar1")
        self.lb4 = QtWidgets.QLabel(self.wg3)
        self.lb4.setGeometry(QtCore.QRect(11, 39, 421, 16))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.lb4.setFont(font)
        self.lb4.setText("")
        self.lb4.setAlignment(QtCore.Qt.AlignCenter)
        self.lb4.setObjectName("lb4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pb2.setText(_translate("MainWindow", "Excel DB"))
        self.pb1.setText(_translate("MainWindow", "폴더 선택"))
        self.lb2.setText(_translate("MainWindow", "소스 : "))
        self.pb3.setText(_translate("MainWindow", "언어 선택"))
        self.rb1.setText(_translate("MainWindow", "on"))
        self.rb2.setText(_translate("MainWindow", "off"))
        self.lb3.setText(_translate("MainWindow", "영상 추가 : "))
        self.pb4.setText(_translate("MainWindow", "변환 시작"))
        self.lb1.setText(_translate("MainWindow", "타입 : "))
        self.label.setText(_translate("MainWindow", "코드 : "))
        self.mainTitle.setText(_translate("MainWindow", "Martian"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
