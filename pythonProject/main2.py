import sys

import qdarkstyle
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

from RC.tablewidgetDrag import tableDragDrop
from setExePath import resource_path1
from ui.root import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        # super(MyMainWindow, self).__init__(parent)
        # self.setupUi(self)
        self.initUI()
        # 외부 클래스에서 드래그 드랍 호출
        table = tableDragDrop(self.tw1)

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

        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

        # 위젯 작동 시키기
        self.execWidget()

    def execWidget(self):
        pass


"""if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())"""
