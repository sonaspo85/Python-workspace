# -*- coding: utf8 -*-
import os.path
import traceback
from shutil import ExecError
from pathlib import Path
from libs.Common.commonVar import common
from libs.idmlController.changeExtIdmltZip import changeExtIdmltZip
from libs.otherController.docInfo import docInfo


class stepOne(common):
    srcDirFullpath = []

    def __init__(self, pbar1, lb4):
        super().__init__()
        self.pbar1 = pbar1
        self.lb4 = lb4

    def runStepOne(self):
        print("runStepOne 시작")

        try:
            # 2. 인터페이스 상의 언어 목록으로 절대 경로 생성 하기
            self.SelectedLangFullPath()

            # 3. 새롭게 저장될 zipDir 폴더 생성
            common.createNewDir(self.zipDir)
            # 4. idml 폴더를 루프하여, idml 파일을 zip 확장자로 변경, zip 폴더로 복사 하기
            ceiz = changeExtIdmltZip(self.pbar1, self.lb4)
            ceiz.loopIdml()

        except Exception as e:
            raise

        else:
            self.pbar1.setValue(35)
            self.lb4.setText("runStepOne 완료")

    def SelectedLangFullPath(self):
        print("SelectedLangFullPath 시작")

        try:
            # 1. 인터페이스에서 선택한 언어 목록 폴더를 절대 경로로 생성
            for langcode in self.workISO:
                # 2. 각 소스 경로를 fullpath로 생성
                self.fullpath = Path(self.srcPath, langcode)
                print("self.fullpath:", self.fullpath)

                stepOne.srcDirFullpath.append(self.fullpath)
            # 3. 절대 경로로 생성한 소스 폴더를 common 모듈의 srcDirFullpath 객체로 수집
            common.srcDirFullpath.extend(stepOne.srcDirFullpath)

        except Exception as e:
            msg = "절대 경로 생성 실패"

            raise Exception(msg)

        else:
            print("SelectedLangFullPath 완료")
            self.pbar1.setValue(10)
            self.lb4.setText("SelectedLangFullPath 완료")

        # 4. 문서 정보를 파일로 추출
        try:
            self.docInfo = docInfo()
            self.docInfo.runExtractXML()

        except Exception as e:
            raise

        else:
            self.pbar1.setValue(20)
            self.lb4.setText("docInfo 완료")
