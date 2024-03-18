# -*- coding: utf8 -*-
import traceback

import qdarktheme
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtWidgets import QApplication, QLabel, QHBoxLayout

from libs.RC.mainWindow import mainWindow
from setExePath import *


def showStartScreen():
    print('showStartScreen 시작')

    # png image
    imgpath = resource_path1('libs/UI/icon.png')
    image = QPixmap(imgpath)

    # 스플래시 이미지 위로 GIF를 넣을 수 있도록 레이아웃을 설정
    layout = QHBoxLayout()

    # QLabel 객체 생성
    image_container = QLabel()
    image_container.setAttribute(Qt.WA_DeleteOnClose)
    image_container.setWindowFlag(Qt.SplashScreen, Qt.FramelessWindowHint)
    # QLabel 객체가 할당될 레이아웃 객체 지정
    image_container.setLayout(layout)
    # QPixmap 이미지 객체를 QLabel 객체에 할당
    image_container.setPixmap(image)

    # GIF 이미지가 할당될 QLabel 객체 생성
    label2 = QLabel()
    label2.setStyleSheet("margin-bottom:21px; margin-right:21px")

    gifpath = resource_path1('libs/UI/decent-circle.gif')
    movie = QMovie(gifpath)
    label2.setMovie(movie)

    layout.addWidget(label2, 0, Qt.AlignRight | Qt.AlignBottom)
    movie.start()
    image_container.show()

    return image_container


if __name__ == '__main__':
    try:

        # Enable HiDPI.
        qdarktheme.enable_hi_dpi()

        # Qapplication : 응용 프로그램을 실행 시켜주는 클래스
        app = QApplication(sys.argv)
        # mainWindow 클래스를 인스턴스로 객체로 생성
        mainwindow = mainWindow()

        # Apply dark theme.
        qdarktheme.setup_theme(custom_colors={"primary": "#e6fa98"})

        splash_screen = showStartScreen()
        QTimer.singleShot(2 * 1000, splash_screen.close)
        QTimer.singleShot(2000, mainwindow.show)

        # 인터페이스 동작
        app.exec()


    except Exception as e:
        # print('error: ', e)
        print(traceback.format_exc())