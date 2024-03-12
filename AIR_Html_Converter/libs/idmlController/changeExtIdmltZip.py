# -*- coding: utf8 -*-
import os
import shutil
import traceback
from pathlib import Path
from libs.Common.commonVar import common


class changeExtIdmltZip(common):
    def __init__(self, pbar1, lb4):
        self.pbar1 = pbar1
        self.lb4 = lb4

    def loopIdml(self):
        print("loopIdml 시작")

        for srcdir in self.srcDirFullpath:
            fullpath = srcdir

            # 1. 폴더가 존재 하는지 확인
            if os.path.exists(srcdir):
                try:
                    idmldir = os.listdir(srcdir)
                    # print(f'{idmldir}')
                    # 2. 각각의 언어코드내 탐색
                    for dir2 in idmldir:
                        # 3. 절대 경로 생성
                        abpath = os.path.join(fullpath, dir2)
                        # 4. 파일이름 추출
                        filename2 = dir2
                        # idml 폴더의 바로위 부모 iso 값 추출
                        self.absparDir = os.path.dirname(abpath)
                        # split() 함수의 매개값으로 파일명을 제외한 바로위 절대 폴더 경로 할당
                        self.isocode = os.path.split(self.absparDir)[1]

                        # 5. idml 파일인 경우
                        if os.path.isfile(abpath) and abpath.endswith(".idml"):
                            # splitext() : 파일이름과 확장자 분리
                            name, ext = os.path.splitext(filename2)
                            # self.nameNiso = (name, self.isocode)
                            self.nameNiso[name] = self.isocode

                            # 6. zipDir 경로에 .zip 확장자로 저장하기 위해 새로운 경로 생성
                            newfilename = name + ".zip"
                            newzipPath = Path(self.zipDir / newfilename)

                            # 7. zipDir 경로에 zip 으로 확장자 변경후 복사하기
                            shutil.copy(abpath, newzipPath)

                        elif os.path.isdir(abpath):
                            self.isoNimgTuple = (self.isocode, abpath)
                            common.isoNimgTuple = self.isoNimgTuple

                except Exception as e:
                    msg = "idml to zip 변환 실패"
                    raise Exception(msg)

                else:
                    self.pbar1.setValue(30)
                    self.lb4.setText("zipDir 경로 zip 생성 완료")

        print("loopIdml 완료!!")
