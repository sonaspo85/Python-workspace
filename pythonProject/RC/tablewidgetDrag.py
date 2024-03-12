from PyQt5 import QtCore
from PyQt5.QtWidgets import *


# 외부 클래스에서 드래그 드랍을 구현 하기 위해서는 QtCore.QObject를 상속 받아야 한다.
class tableDragDrop(QtCore.QObject):
    def __init__(self, ui):
        # 매개변수로 전달 받는 ui는 QTableWidget 객체임
        super().__init__(ui)

        self.tw1 = ui

        # viewport 란 TableWidget의 전체 항목 영역을 말한다.
        # installEventFilter(self): tableWidget 의 viewport 영역에 이벤트 필터를 설치 한다.
        # 이벤트 필터는 tableWidget 의 viewport 영역로 전송되는 모든 이벤트를 수신하는 객체이다.
        self.tw1.viewport().installEventFilter(self)
        # setRowCount(): 현재 TableWidget의 행의 개수를 0개로 설정
        self.tw1.setRowCount(0)
        # setColumnCount(): 현재 TableWidget의 열의 개수를 1개로 설정
        self.tw1.setColumnCount(1)

    def eventFilter(self, source, event):
        print("eventFilter 시작")

        if (
            source is self.tw1.viewport()
            and (
                event.type() == QtCore.QEvent.DragEnter
                or event.type() == QtCore.QEvent.DragMove
                or event.type() == QtCore.QEvent.Drop
            )
            and event.mimeData().hasUrls()
        ):
            if event.type() == QtCore.QEvent.Drop:
                # urls: MIME 데이터 객체 내에 포함된 URL 목록을 반환
                for url in event.mimeData().urls():
                    if url.isLocalFile():
                        # addFile() 함수 호출
                        self.addFile(url.path())
            event.accept()
            return True
        return super().eventFilter(source, event)

    def addFile(self, filepath):
        print("addFile 시작")
        row = self.tw1.rowCount()
        print("row:", row)
        # insertRow(row): 매개값으로 주어진 인덱스에 row를 삽입
        self.tw1.insertRow(row)
        # QTableWidget 에 항목 데이터를 삽입하기 위해서는 QTableWidgetItem 형식의 객체로 삽입 되어야 한다.
        item = QTableWidgetItem(filepath)
        # setItem(row, col, item): row, col 위치에 항목을 추가 한다.
        # 현재는 col이 1개 밖에 없기 때문에 0으로 입력됨
        self.tw1.setItem(row, 0, item)
        # 입력된 path의 길이에 따라 tablewidget 의 col 너비가 변경됨
        self.tw1.resizeColumnToContents(0)

    def no_file_selected(self):
        print("no_file_selected 시작")

        # QMessageBox 팝업 알림창을 띄우기 위해 QMessageBox 객체 생성
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("파일을 선택 하지 않았습니다.")
        msg.setWindowTitle("Warning 타이틀!")
        retval = msg.exec_()

    def process_completed(self):
        print("process_completed 시작")

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("파일 선택이 완료 되었습니다.")
        msg.setWindowTitle("Completed 타이틀!")
        retval = msg.exec_()
