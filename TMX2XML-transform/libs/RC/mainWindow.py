# -*- coding: utf8 -*-
import shutil
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
        self.srcpath = ''

        # root.py 파일내 선언된 위젭 및 컨테이너에 접근
        self.setupUi(self)
        self.initUI()
        # ui 윈도우창 출력
        self.show()
        self.projectDir = Path(resource_path2('')).absolute().as_posix()



    def initUI(self):
        print('initUI 시작')

        self.setWindowTitle("tmx2xml-transform")
        self.setFixedSize(344, 296)

        # 메인 윈도우창 상단바에 아이콘 넣기
        iconpath = resource_path1('libs/UI/icon.png')
        print(f'{iconpath=}')
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
            try:
                if self.srcpath == '':
                    self.srcpath = self.le1.text()

                # print('self.srcpath111:', self.srcpath)

                # 선택한 디렉토리 반복
                setfilenlang = setfileNlang(self.srcpath)
                self.dic_map = setfilenlang.setDict()


            except Exception as e:
                print(traceback.format_exc())



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
                # 폴더 삭제
                try:
                    tempD = os.path.join(self.projectDir, 'temp')
                    jsonD = os.path.join(self.projectDir, 'json')

                    if os.path.isdir(tempD):
                        shutil.rmtree(tempD)

                    elif os.path.isdir(jsonD):
                        shutil.rmtree(jsonD)

                except Exception as e:
                    msg = 'temp, json 폴더 삭제 실패'
                    self.getErrorPopup(msg)

                else:
                    self.pbar1.setValue(30)
                    self.lb2.setText("레거시 temp, json 폴더 삭제 완료")

                # xslt 실행
                try:
                    trans = transformXSLT(self.dic_map, self.pbar1, self.lb2)
                    trans.set_sequence()
                    # trans.runXSLT()


                except Exception as e:
                    msg = 'xslt 변환 실패'
                    self.getErrorPopup(msg)
                    return

                else:
                    self.pbar1.setValue(90)
                    self.lb2.setText("xslt 변환 성공")

                # ftp 업로드
                try:
                    ftp = ftpClass(ftpfolder)
                    ftp.runFTP()

                except Exception as e:
                    msg = 'ftp 업로드 실패'
                    self.getErrorPopup(msg)
                    return

                else:
                    self.pbar1.setValue(100)
                    self.lb2.setText("ftp 업로드 성공")


                # temp 폴더 삭제
                try:
                    shutil.rmtree(self.projectDir + '/temp/')

                except Exception as e:
                    msg = 'temp 폴더 삭제 실패'
                    self.getErrorPopup(msg)
                    return

                else:
                    self.pbar1.setValue(100)
                    self.lb2.setText("temp 폴더 삭제 성공")

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


    def getErrorPopup(self, msg, title_txt="에러 팝업 창"):
        print("getErrorPopup 시작")

        self.msgbox = QMessageBox()
        self.msgbox.setWindowTitle(title_txt)

        # 상단바에 아이콘 넣기
        iconpath = resource_path1('libs/UI/icon.png')
        qicon = QIcon(iconpath)
        # QMessageBox 상단바에 아이콘 넣기
        self.msgbox.setWindowIcon(qicon)

        # QMessageBox 내부에 표시될 아이콘
        self.msgbox.setText(msg)
        # self.msgbox.setInformativeText(msg)
        # QMessageBox의 버튼
        self.msgbox.setStandardButtons(QMessageBox.Ok)
        # 포커스가 지정된 기본 버튼
        self.msgbox.setDefaultButton(QMessageBox.Ok)
        # QMessageBox 클릭한 버튼 결과 반환
        self.retval = self.msgbox.exec()
        # print('self.retval: ', self.retval)


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
            fname = QFileDialog.getExistingDirectory(self, '소스 폴더를 선택해 주세요.')
            # fname = "H:/Workspace/Python-workspace/TMX2XML-transform/resource"
            # 입력 받은 문자열 경로를 Path 객체로 변환
            self.srcpath = Path(fname).absolute().as_posix()
            self.le1.setText(self.srcpath)


        except Exception as e:
            print(traceback.format_exc())


