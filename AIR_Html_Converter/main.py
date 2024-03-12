import socket
import time

import qdarktheme
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFontDatabase, QFont, QPixmap, QMovie
from PyQt5.QtWidgets import QApplication, QLabel, QHBoxLayout
from qtpy import QtGui

from libs.RC.mainWindow import MainWindow
from libs.Ui.customWinStyle import customWinStyle as css
from libs.otherController.connectFTP import connectFTP
from setExePath import *


def showStartScreen():
    start = time.time()

    # PNG image
    img_path = resource_path1("libs/Ui/Splash.png")
    image = QPixmap(img_path)

    # set layout in order to put GIF in above (on top) a word that are in splash image
    layout = QHBoxLayout()

    # big image for Splash screen
    image_container = QLabel()
    image_container.setAttribute(Qt.WA_DeleteOnClose)
    image_container.setWindowFlag(Qt.SplashScreen, Qt.FramelessWindowHint)
    image_container.setLayout(layout)
    image_container.setPixmap(image)

    # label for displaying GIF
    label_2 = QLabel()
    label_2.setStyleSheet("margin-bottom:21px; margin-right:21px")

    gif_path = resource_path1("libs/Ui/decent-circle.gif")
    movie = QMovie(gif_path)
    label_2.setMovie(movie)

    layout.addWidget(label_2, 0, Qt.AlignRight | Qt.AlignBottom)
    movie.start()
    image_container.show()

    return image_container


@staticmethod
def downloadresource():
    print("downloadresource 시작")

    # 현재 접속 중인 PC 이름 추출
    pcname = socket.gethostname()

    if pcname.find("T5BM6DO") == -1:
        print("다운로드 시작!!!")
        # resource 경로로 xslt 및 엑셀 템플릿 다운 받기
        projectDir = resource_path2("")
        print("projectDir111:", projectDir)

        # resource 경로
        resourceDir = projectDir + "resource"

        ftpdir = "/tcs/confidential/CE-HTML-Converter/resource"

        connectftp = connectFTP()
        connectftp.runFTP(ftpdir, resourceDir)


if __name__ == "__main__":
    try:
        # resource 경로로 xslt 및 엑셀 템플릿 다운 받기
        downloadresource()

        time.sleep(0.2)

        # Enable HiDPI.
        qdarktheme.enable_hi_dpi()

        # Qapplication : 응용 프로그램을 실행 시켜 주는 클래스
        app = QApplication(sys.argv)

        # 폰트 로드
        ttfpath = resource_path1("libs/Ui/사각사각.otf")
        fontdb = QFontDatabase()
        fontid = fontdb.addApplicationFont(ttfpath)
        ttffont = QFont("one of your font families")
        print("폰트 이름: ", QtGui.QFontDatabase.applicationFontFamilies(fontid))

        # Apply dark theme.
        qdarktheme.setup_theme(additional_qss=css.qss)

        # MainWindow 클래스를 인스턴스 객체로 생성
        mainWindow = MainWindow()
        splash_screen = showStartScreen()
        QTimer.singleShot(3 * 1000, splash_screen.close)
        QTimer.singleShot(3000, mainWindow.show)

        # 프로그램 작동
        app.exec()

    except Exception as e:
        print("error:", e)
