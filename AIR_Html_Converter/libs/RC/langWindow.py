from PyQt5.QtCore import QSize
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QListWidgetItem

from libs.Ui.langPop import Ui_Form
from setExePath import *


class langWindow(QWidget, Ui_Form):
    sig = pyqtSignal()

    def closeEvent(self, event):
        print("팝업 윈도우창 닫힘")
        self.sig.emit()

    # 초기화
    def __init__(self, langMap):
        super().__init__()  # 부모 클래스의 속성들에 접근하기 위해 필요

        self.langMap = langMap

        # 2. 인스턴스 함수 호출
        self.initUI()

    def initUI(self):
        print("initUI 시작")

        self.setupUi(self)
        self.setWindowTitle("langPopup창 출력")
        self.setFixedSize(341, 312)
        # 팝업 윈도우창 상단바에 아이콘 넣기
        self.iconpath = resource_path1("libs/Ui/xxx.ico")
        self.qicon = QIcon(self.iconpath)
        self.setWindowIcon(self.qicon)

        # list Widget 에 언어 목록 입력 하기
        self.setLanguage()

    def setLanguage(self):
        print("setLanguage 시작")

        try:
            for item in self.langMap.keys():
                self.item = QListWidgetItem(item)
                self.item.setSizeHint(QSize(0, 20))
                self.plw1.addItem(self.item)

        except Exception as e:
            print("error:", e)
