# -*- coding: utf8 -*-
import re

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

from lxml import etree as et
from readmailContent import readContent
from sandOutlook import outlookController
from setExePath import *
from ui.root import Ui_MainWindow


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

    def saveF(self):
        print("saveF 시작")

        # print(f'{self.getTitle=}')
        print(f"{self.te2.toPlainText()}")

        self.writeData(self.te1.text(), self.te2.toPlainText())

    def sandmail(self):
        print("sandmail 시작")
        try:
            self.getlist = self.listview2
            # 총 개수 파악
            self.totalcnt = self.getlist.count()

            self.personL = []
            for i in range(self.totalcnt):
                self.getitem = self.listview2.item(i).text()
                self.personL.append(self.getitem)

            self.getTitle = self.te1.text()
            # print('self.getTitle:', self.getTitle)

            self.getTxtBrow = self.te2.toPlainText()
            # print('self.getTxtBrow: ', self.getTxtBrow)

            self.writeData(self.getTitle, self.getTxtBrow)

            # 메일 보내기
            so = outlookController()
            so.runOutlook(self.personL)

            self.Warning_event()

        except Exception as e:
            print("error:", e)

    def Warning_event(self):
        self.buttonReply = QMessageBox.warning(
            self, "메일 보내기", "메일 보내기가 완료 되었습니다.!", QMessageBox.Ok
        )

        if self.buttonReply == QMessageBox.Ok:
            print("Yes clicked.")

    def writeData(self, getTitle, getTxtBrow):
        print("writeData 시작")

        # print(f'{self.contentF=}')
        if os.path.isfile(self.contentF):
            print("파일이 존재 합니다.")
            # 1. html 파서전 파서 옵션 지정
            parser = et.HTMLParser(encoding="utf8", recover=True)
            # 2. html 문서 파서
            doc = et.parse(self.contentF, parser)
            # 3. 문서내 root 요소에 접근
            root = doc.getroot()

            for child in root.iter():
                if child.tag == "title":
                    print("getTitle:", getTitle)
                    child.text = getTitle

                elif child.tag == "body":
                    child.text = getTxtBrow

            doc.write(self.contentF, pretty_print=True, encoding="utf-8", method="html")

    def readF(self):
        print("readF 시작")
        try:
            self.getItem = self.listview1.currentItem().text()

            form = resource_path1("resource")
            self.contentF = form + "/" + self.getItem + ".html"
            print("self.contentF:", self.contentF)

            if os.path.isfile(self.contentF):
                # self.te1.clear()
                self.te2.clear()

                readC = readContent()
                readC.readHtmlF(self.contentF)

                self.getTitle = readC.titleContent
                self.getBody = readC.result

                self.te1.setText(self.getTitle)

                for content in self.getBody:
                    a = re.sub("\r", "", content)
                    print(a)
                    self.te2.append(a)

            self.listview1.currentItemChanged.connect(self.saveF)

        except Exception as e:
            print("error:", e)
