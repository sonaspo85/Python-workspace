# -*- coding: utf8 -*-
import re

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *


from readmailContent import readContent
from setExePath import *
from ui.root import Ui_MainWindow
from sandOutlook import outlookController


# 1. 화면을 띄우는데 사용되는 class 선언
class MainWindow(QMainWindow, Ui_MainWindow):
    # 초기화
    def __init__(self):
        super().__init__()  # 부모 클래스의 맴버들에 접근하기 위해 사용

        self.setupUi(self)

        # 2. 인스턴스 함수 호출
        self.initUI()

    def initUI(self):
        # setupUi() : ui.py 로 작성된 위젯 및 컨테이너에 접근 하여 각 위젯들을 스크립트 환경에서 접근할 수 있다.
        self.setupUi(self)

        # 메인 UI 윈도우의 타이틀바 제목 및 사이즈 설정
        self.setWindowTitle("QDateTimeEdit 테스트!!")

        # setGeometry(): 메인 윈도우 창의 위치와 크기 결정
        # self.setGeometry(0, 0, 400, 400)

        # 어플 상단바에 아이콘 넣기
        # QIcon 객체 생성, setWindowIcon() 함수의 매개값으로 QIcon 객체 할당하기
        iconpath = resource_path1("ui/xxx.ico")
        qicon = QIcon(iconpath)
        self.setWindowIcon(qicon)

        # 위젯 작동 시키기
        self.execWidget()

    def execWidget(self):
        self.listview1.itemClicked.connect(self.readF)

        self.pb1.clicked.connect(self.sandmail)

    def sandmail(self):
        print("sandmail 시작")

        self.getlist = self.listview2
        # 총 개수 파악
        self.totalcnt = self.getlist.count()

        self.personL = []
        for i in range(self.totalcnt):
            self.getitem = self.listview2.item(i).text()
            self.personL.append(self.getitem)

        self.getTitle = self.te1.toPlainText()
        # print('self.getTitle:', self.getTitle)

        self.getTxtBrow = self.tb1.toPlainText()
        # print('self.getTxtBrow: ', self.getTxtBrow)

        # 메일 보내기
        so = outlookController()
        so.runOutlook(self.personL, self.getTitle, self.getTxtBrow)

    def readF(self):
        print("readF 시작")

        self.getItem = self.listview1.currentItem().text()
        # print('self.getItem:', self.getItem)
        form = resource_path1("resource")
        print("form111:", form)
        self.contentF = "G:/Test/test/" + self.getItem + ".html"

        if os.path.isfile(self.contentF):
            self.tb1.clear()
            self.tb1.clear()

            readC = readContent()
            readC.readHtmlF(self.contentF)

            self.getTitle = readC.titleContent
            self.getBody = readC.result

            self.te1.setText(self.getTitle)

            for content in self.getBody:
                a = re.sub("\r", "", content)
                print(a)
                self.tb1.append(a)
