# -*- coding: utf8 -*-

from RC.mainWindow import *
from ui.root2 import Ui_Form2
from setExePath import *


# 1. 화면을 띄우는데 사용되는 class 선언
class SubWindow(QMainWindow, Ui_Form2):
    # 초기화
    def __init__(self):
        super().__init__()  # 부모 클래스의 맴버들에 접근하기 위해 사용

        # 2. 인스턴스 함수 호출
        self.initUI()

    def initUI(self):
        # setupUi() : ui.py 로 작성된 위젯 및 컨테이너에 접근 하여 각 위젯들을 스크립트 환경에서 접근할 수 있다.
        self.setupUi(self)

        # 메인 UI 윈도우의 타이틀바 제목 및 사이즈 설정
        self.setWindowTitle("SubWindows 창 출력!!!")

        # 어플 상단바에 아이콘 넣기
        # QIcon 객체 생성, setWindowIcon() 함수의 매개값으로 QIcon 객체 할당하기
        iconpath = resource_path1("ui/xxx.ico")
        qicon = QIcon(iconpath)
        self.setWindowIcon(qicon)

        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
