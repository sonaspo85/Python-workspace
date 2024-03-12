# -*- coding: utf8 -*-
import os
import traceback
import zipfile
from pathlib import Path

from libs.Common.commonVar import common


class stepTwo(common):
    unziPath = ""
    msg = ""

    def __init__(self, pbar1, lb4):
        super().__init__()

        self.pbar1 = pbar1
        self.lb4 = lb4

    def unzip(self):
        print("unzip 시작")

        try:
            # os.listdir(): zipDir 디렉토리내 zip파일들을 경로 없는 파일이름만으로 요소를 생성하여 list로 수집
            # self.zipDir: zipDir 디렉토리 전체 경로
            self.tuple1 = (os.listdir(self.zipDir), self.zipDir)
            # 3. 리스트 객체인데 각 요소들이 튜플
            self.zipdirs = [self.tuple1]

            self.zipInFiles = self.zipdirs[0][0]
            self.zipDir = self.zipdirs[0][1]

            for eachZF in self.zipInFiles:
                zipname, ext = os.path.splitext(eachZF)
                self.abpath = Path(self.zipDir / eachZF)

                stepTwo.unziPath = Path(self.zipDir / zipname)
                print("stepTwo.unziPath:", stepTwo.unziPath)

                with zipfile.ZipFile(self.abpath, mode="r") as zip:
                    # namelist() : zip 파일내 중첩된 모든 파일 및 폴더를 반환
                    ziplist = zip.namelist()

                    for zipdir in ziplist:
                        # 디렉토리 이름 추출
                        parDirname = os.path.dirname(zipdir)
                        # xml파일 인데, 부모 폴더가 Stories 이거나 자신의 파일 이름이 designmap.xml 인 경우
                        if zipdir.endswith(".xml") and (
                            parDirname.find("Stories") > -1
                            or zipdir.find("designmap.xml") > -1
                        ):
                            zip.extract(zipdir, stepTwo.unziPath)

        except Exception as e:
            msg = "unzip 실패"
            raise Exception(msg)

        else:
            self.pbar1.setValue(40)
            self.lb4.setText("unzip 완료")

        # 5. zipDir 폴더내 zip 확장자 파일들 삭제
        try:
            self.dirs = os.listdir(self.zipDir)

            for file in self.dirs:
                # 1. 절대 경로 생성
                abpath = Path(self.zipDir, file)
                # 2. zip 파일 삭제
                if file.endswith(".zip"):
                    os.remove(abpath)

        except Exception as e:
            msg = "zip 파일 삭제 실패"
            raise Exception(msg)

        else:
            self.pbar1.setValue(45)
            self.lb4.setText("zipDir 폴더내 zip 파일 삭제 완료")
