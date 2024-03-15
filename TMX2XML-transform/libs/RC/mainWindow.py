# -*- coding: utf8 -*-
import traceback

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox

from libs.UI.root import Ui_MainWindow
from libs.controller.ftpcontroller import ftpClass
from libs.controller.transformXSLT import transformXSLT
from setExePath import *

from pathlib import Path
from libs.controller.readTeam import readTeam
from libs.controller.readCodesF import readCodeF
from libs.controller.setfileNlang import setfileNlang


class mainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        # 부모 클래스의 속성에 접근
        super().__init__()

        self.teamL = []
        self.srcpath = ''
        self.dic_map = {}

        # root.py 파일내 선언된 위젭 및 컨테이너에 접근
        self.setupUi(self)
        self.initUI()
        # ui 윈도우창 출력
        self.show()



    def initUI(self):
        print('initUI 시작')

        self.setWindowTitle("tmx2xml-transform")
        self.setFixedSize(338, 232)

        # 메인 윈도우창 상단바에 아이콘 넣기
        iconpath = resource_path1('libs/UI/icon.png')
        print(f'{iconpath=}')
        # 상단바에 아이콘을 삽입하기 위해서는 setWindowIcon() 객체의 매개값으로 QIcon 객체가 할당되어야 한다.
        qicon = QIcon(iconpath)
        self.setWindowIcon(qicon)

        # 위젯 작동 시키기
        self.initialize()


    def initialize(self):
        print('initialize 시작')

        #  파트 목록 추가
        # team.xml 파일 읽기
        self.readTeamF()

        self.bt2.clicked.connect(self.openDialog)
        self.bt1.clicked.connect(self.btStart)


    def btStart(self):
        print('btStart 시작')

        try:
            cobotxt = self.cb1.currentText()
            txtfield = self.le1.text()
            print(f'{self.dic_map=}')

            ftpfolder = ''
            for tuple in self.teamL:
                team = tuple[0]
                folder = tuple[1]

                if team == cobotxt:
                    ftpfolder = folder


            if cobotxt != '' and txtfield != '' and len(self.dic_map) > 0:
                # xslt 실행
                try:
                    trans = transformXSLT(self.dic_map)
                    trans.set_sequence()
                    trans.runXSLT()


                except Exception as e:
                    print('error:', traceback.format_exc())


                # ftp 업로드
                try:
                    ftp = ftpClass(cobotxt)
                    ftp.runFTP()

                except Exception as e:
                    print('error:', traceback.format_exc())


            else:
                print('파트, 소스 경로 모두 입력해주세요.')

                msgbox = QMessageBox()
                msgbox.setWindowTitle('오류가 발생 되었습니다.')
                iconpath = resource_path1('UI/icon.png')
                qicon = QIcon(iconpath)
                msgbox.setWindowIcon(qicon)

                msgbox.setText('파트, 소스 경로 모두 입력해주세요.')
                msgbox.setStandardButtons(QMessageBox.Ok)

                msgbox.exec_()


        except Exception as e:
            print('error:', traceback.format_exc())

        else:
            QMessageBox.information(self, '작업완료', '작업이 완료 되었습니다.', QMessageBox.Ok)



    def readTeamF(self):
        print('readTeamF 시작')

        readteam = readTeam()
        self.teamL = readteam.runRead()
        print(f'{self.teamL=}')

        # 리스트 표현식으로 팀목록 추가
        # [self.cb1.addItem(x) for x in self.teamL]

        for tuple in self.teamL:
            type = tuple[0]

            self.cb1.addItem(type)




    def read_codesF(self):
        print('read_codesF 시작')

        readCodef = readCodeF()
        readCodef.runReadCodes()



    def openDialog(self):
        print('openDialog 시작')

        try:
            # 폴더 다이얼로그
            # fname = QFileDialog.getExistingDirectory(self, '소스 폴더를 선택해 주세요.')
            fname = "H:/Workspace/Python-workspace/TMX2XML-transform/resource"
            # 입력 받은 문자열 경로를 Path 객체로 변환
            self.srcpath = Path(fname).absolute().as_posix()
            self.le1.setText(self.srcpath)


        except Exception as e:
            print(traceback.format_exc())


        try:
            # 선택한 디렉토리 반복
            setfilenlang = setfileNlang(self.srcpath)
            self.dic_map = setfilenlang.setDict()





        except Exception as e:
            print(traceback.format_exc())