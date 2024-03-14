# -*- coding: utf8 -*-
import shutil
import traceback
import re
import subprocess

from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QRadioButton, QMessageBox, QFileDialog, QMenu
from pathlib import Path
from libs.Common.commonVar import common
from libs.RC.langWindow import langWindow
from libs.Ui.root import Ui_MainWindow
from libs.excelColntroller.stepFive import stepFive
from libs.idmlController import stepThree
from libs.otherController import langsDB
from libs.otherController.connectFTP import connectFTP
from libs.otherController.copyImges import copyImages
from libs.otherController.stepSix import stepSix
from libs.zipController import stepOne, stepTwo
from setExePath import *


class MainWindow(QMainWindow, Ui_MainWindow):
    selectedItems = []
    pbarcnt = 0

    def __init__(self):
        super().__init__()  # 부모 클래스의 속성들에 접근하기 위해 사용

        # ui.py 파일내 선언된 위젯 및 컨테이너에 접근하기 위한 함수
        self.setupUi(self)
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Martian")
        # 메인 윈도우창 리사이즈 금지
        self.setFixedSize(494, 298)

        # 메인 윈도우창 상단바에 아이콘 넣기
        # QIcon 객체 생성, setWindowIcon() 함수의 매개값으로 QIcon 객체 할당 하기
        self.iconpath = resource_path1("libs/Ui/xxx.ico")
        print(f"{self.iconpath=}")
        self.qicon = QIcon(self.iconpath)
        self.setWindowIcon(self.qicon)

        # 위젯 작동 시키기
        self.initialize()


    def initialize(self):
        print("initialize 시작")

        # 1. 초기 디렉토리 설정
        self.setDirectoryPath()

        # 2. 언어 목록 엑셀을 xml로 변환
        langdb = langsDB()
        langdb.runExtractlang()

        # 3. type.xml 파일 읽기
        langdb.loadType()

        # 4. language.xml 파일 읽기
        langdb.loadLangs()

        # 5. langdb 객체에서 생성한 리스트와 딕셔너리 반환 받기
        self.typeL = []
        self.langMap = {}
        self.typeL, self.langMap = langdb.getListNmap()

        # print(f'{self.typeL=}')
        # print(f'{self.langMap=}')

        # 6. 콤보 박스 채우기
        self.setComboitem()
        # 7. lang 팝업창 띄우기
        self.pb3.clicked.connect(self.openLangPop)
        # 8. video link 엑셀 파일 열기
        self.pb2.clicked.connect(self.runExcel)

        # Excel DB 우클릭시 menu 버튼 뜨기
        self.pb2.customContextMenuRequested.connect(self.on_context_menu)

        self.menu = QMenu(self)
        self.menu.addAction("서버로 업데이트", self.ftpUpload)

        # 9. 폴더 다이얼로그 열기
        self.pb1.clicked.connect(self.openDialogDir)

        # 10. HTML 출력 프로세스 실행
        self.pb4.clicked.connect(self.runStart)

        # 추후 하기 하기 두 목록 삭제 하기

        self.le1.setText("H:/Workspace/Python-workspace/AIR_Html_Converter/srcDir")
        self.rb2.setChecked(True)


    def on_context_menu(self, point):
        print("on_context_menu 시작")

        # show context menu
        self.menu.exec_(self.pb2.mapToGlobal(point))


    def ftpUpload(self):
        print("ftpUpload 시작")
        self.ftppath = "/tcs/confidential/CE-HTML-Converter/resource/excel-template"
        self.excelF = resource_path2("resource/excel-template/template1.xlsx")

        try:
            connectftp = connectFTP()
            connectftp.uploadF(self.ftppath, self.excelF)

        except Exception as e:
            msg = str(e)
            print("error msg:", msg)
            self.getErrorPopup(msg)

        else:
            self.msg = "업로드 완료 했습니다."
            self.getErrorPopup(self.msg, title_txt="완료 팝업창")


    def runStart(self):
        print("runStart 시작")
        # 10. 라디오 선택 목록 추출
        self.boxElements = self.groupBox.children()
        self.radioTxt = ""

        for elem in self.boxElements:
            if isinstance(elem, QRadioButton) and elem.isChecked():
                self.radioTxt = elem.text()

        # ComboBox 선택 목록 추출
        self.typeTxt = self.cb1.currentText()
        # le 에 입력된 값 가져 오기
        self.leTxt = self.le1.text()
        # print('self.leTxt:', self.leTxt)
        if common.srcPath == "":
            common.srcPath = self.leTxt

        # 모델 번호
        common.modelNum = self.le2.text()

        try:
            # 선택 목록이 하나라도 선택되어 있지 않은 경우 메시지 박스 출력
            if self.radioTxt == "" or self.typeTxt == "" or common.modelNum == "":
                self.openmsgbox()

            else:  # 프로그램 작동 진행
                print("self.typeTxt:", self.typeTxt)
                print(f"{self.radioTxt=}")

                # temp 경로
                self.tempDir = Path(common.srcPath, "temp")
                common.tempDir = self.tempDir
                # zipDir 경로
                self.zipDir = Path(common.tempDir, "zipDir")
                common.zipDir = self.zipDir

                common.radioTxt = self.radioTxt
                common.typeTxt = self.typeTxt

                # UI에서 선택한 언어의 언어 코드를 추출
                self.getISO()
                self.stWork()

        except Exception as e:
            self.msg = traceback.format_exc()
            print(self.msg)


    def stWork(self):
        print("startWork 시작")

        # 1.idml 파일을 zip 확장자로 변경하고 UI에서 선택한 언어만 절대 경로로 추출
        try:
            stepone = stepOne(self.pbar1, self.lb4)
            stepone.runStepOne()

        except Exception as e:
            msg = str(e)
            print("error msg:", msg)
            self.getErrorPopup(msg)

        # 2. unzip 하기
        try:
            steptwo = stepTwo(self.pbar1, self.lb4)
            steptwo.unzip()

        except Exception as e:
            msg = str(e)
            print("error msg:", msg)
            self.getErrorPopup(msg)

        # 3. zipDir 폴더내 각 폴더내에 접근하기
        try:
            stepthree = stepThree(self.pbar1, self.lb4)
            stepthree.runStepThree()

        except Exception as e:
            msg = str(e)
            print("error msg:", msg)
            self.getErrorPopup(msg)

        # 4. template1.xlsx xml로 변환
        try:
            stepfive = stepFive(self.pbar1, self.lb4)
            stepfive.runStepFive()

        except Exception as e:
            msg = str(e)
            print("error msg:", msg)
            self.getErrorPopup(msg)

        # 5. 각 소스 반복 하여 xslt 돌리기
        try:
            stepsix = stepSix(self.pbar1, self.lb4)
            stepsix.runStepSix()

            # 6. docInfo 업데이트
            stepsix.updateInfo()

        except Exception as e:
            msg = str(e)
            print("error msg:", msg)
            self.getErrorPopup(msg)

        else:
            print("완료!!!")

        # 7. ftp 접속 하여 templates 다운 받기
        try:
            connectftp = connectFTP()
            connectftp.read_workinglngs()

        except Exception as e:
            msg = str(e)
            print("error msg:", msg)
            self.getErrorPopup(msg)

        else:
            self.pbar1.setValue(80)
            self.lb4.setText("FTP 서버로 부터 templates 복사 완료")

        # 8. 이미지 폴더 복사
        try:
            copyimg = copyImages()
            copyimg.runCopyImg()

        except Exception as e:
            msg = str(e)
            print("error msg:", msg)
            self.getErrorPopup(msg)

        else:
            self.pbar1.setValue(90)
            self.lb4.setText("images 폴더 복사 완료")

            # 완료 팝업창 출력
            self.msg = "작업이 완료 되었습니다."
            self.getErrorPopup(self.msg, title_txt="완료 팝업창")

        # 9. temp 폴더 삭제
        try:
            shutil.rmtree(self.tempDir)

        except Exception as e:
            msg = "temp 폴더 삭제 실패"
            print("error msg:", msg)
            self.getErrorPopup(msg)

        else:
            self.pbar1.setValue(95)
            self.lb4.setText("temp 폴더 삭제 완료")


    def progressBarTimer(self):
        # 1. QProgressBar의 현재값을 반환 한다.
        self.time = self.pbar1.value()
        # 2. 반환된 현재값 + 1 하여 time 속성을 1씩 증가
        self.time += 1
        # 3.QProgressBar의 현재값을 1씩 증가된 값으로 재설정
        self.pbar1.setValue(self.time)

        # 4. QProgressBar의 값이 최대값 이상이 되면 Timer를 중단 시켜 ProgressBar의 값이 더이상 증가되지 않도록 설정
        if self.time >= self.pbar1.maximum():
            self.timerVar.stop()


    def openmsgbox(self):
        print("openmsgbox 시작")

        self.msgbox = QMessageBox()
        self.msgbox.setWindowTitle("모든 항목을 선택 해주세요.")

        # QMessageBox 상단바에 아이콘 넣기
        self.msgbox.setWindowIcon(self.qicon)
        # QMessageBox 내부에 표시될 아이콘
        # self.msgbox.setText('모든 항목을 선택해 주세요.')
        self.msgbox.setInformativeText("모든 항목을 선택해 주세요.")
        # QMessageBox의 버튼
        self.msgbox.setStandardButtons(QMessageBox.Ok)
        # 포커스가 지정된 기본 버튼
        self.msgbox.setDefaultButton(QMessageBox.Ok)
        # QMessageBox 클릭한 버튼 결과 반환
        self.retval = self.msgbox.exec()
        print("self.retval: ", self.retval)


    def openDialogDir(self):
        print("openDialogDir 시작")

        try:
            # 다이얼로그 옵션
            self.options = QFileDialog.Options()
            self.options |= QFileDialog.ShowDirsOnly
            # self.options |= QFileDialog.DontUseNativeDialog
            # 폴더 다이얼로그
            self.srcPath = QFileDialog.getExistingDirectory(
                self, "소스 폴더를 선택 해주세요.", options=self.options
            )
            # common.srcPath = self.srcPath
            common.srcPath = Path(self.srcPath)
            # print(f'{self.srcPath=}')
            self.le1.clear()
            self.le1.setText(self.srcPath)

        except Exception as e:
            self.msg = traceback.format_exc()
            print(f"{self.msg=}")


    def runExcel(self):
        print("runExcel 시작")

        try:
            # self.command = common.resourceDir + '/excel-template/template1.xlsx'
            # print('self.command:', self.command)
            self.externalpath = resource_path2("resource/excel-template/template1.xlsx")
            print("self.externalpath:", self.externalpath)

            if os.path.isfile(self.externalpath):
                print("파일이 존재 합니다.")
                self.popen = subprocess.Popen(
                    args=self.externalpath,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    encoding="utf8",
                    shell=True,
                    text=True,
                )

            else:
                print("파일이 존재 하지 않습니다.")
                raise NotImplementedError

        except Exception as e:
            # self.msg = traceback.format_exc()
            # print(f'{self.msg=}')
            self.msg = "파일이 존재 하지 않습니다."
            self.getErrorPopup(self.msg)


    def getErrorPopup(self, msg, title_txt="에러 팝업 창"):
        print("getErrorPopup 시작")

        self.msgbox = QMessageBox()
        self.msgbox.setWindowTitle(title_txt)

        # QMessageBox 상단바에 아이콘 넣기
        self.msgbox.setWindowIcon(self.qicon)
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


    def openLangPop(self):
        print("openLangPop 시작")

        try:
            # 1. mainWindow 창 숨기기
            self.hide()
            # 2. 팝업 윈도우 객체 생성
            self.langwindow = langWindow(self.langMap)
            # 3. 팝업 윈도우 닫힘 감시
            self.langwindow.sig.connect(self.getLangitem)
            self.langwindow.show()

        except Exception as e:
            print("error:", "언어 팝업창 로드 실패")


    def getLangitem(self):
        print("getLangitem 시작")

        # 메인 윈도우창 다시 열기
        self.show()

        self.cnt = self.langwindow.plw2.count()
        # 최종 선택한 언어 리스트 객체로 할당
        for x in range(self.cnt):
            self.item = self.langwindow.plw2.item(x).text()

            MainWindow.selectedItems.append(self.item)


    def setComboitem(self):
        print("setComboitem 시작")
        # 1. 콤보 박스에 type 값을 목록으로 채우기
        for i in self.typeL:
            self.cb1.addItem(i)


    def setDirectoryPath(self):
        print("setDirectoryPath 시작")
        # 현재 프로젝트 디렉토리 경로
        self.projectDir = resource_path2("")
        # common.projectDir = re.sub('\\\\$', '', self.projectDir)

        common.projectDir = Path(self.projectDir)
        print("common.projectDir:", common.projectDir)
        # resource 경로
        resourceDir = common.projectDir / "resource"
        common.resourceDir = resourceDir
        # xsls 경로
        xslsDir = common.resourceDir / "xsls"
        common.xslsDir = xslsDir

        # Excel 템플릿 경로
        excelTemplsDir = common.resourceDir / "excel-template"
        common.excelTemplsDir = excelTemplsDir


    def getISO(self):
        print("getISO 시작")

        # 선택한 언어의 언어 코드 추출
        for lang in MainWindow.selectedItems:
            for lang2 in self.langMap.keys():
                if lang2 == lang:
                    # print('lang2: ', self.langMap.get(lang2))

                    common.workISO.append(self.langMap.get(lang2))
                    common.langMap[lang2] = self.langMap.get(lang2)
