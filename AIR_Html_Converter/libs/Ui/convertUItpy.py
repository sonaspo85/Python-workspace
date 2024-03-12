# -*- coding:utf8 -*-
import subprocess
import traceback

from setExePath import *
from glob import glob


class convertuiTpy:
    def setpath(self):
        print("setpath 시작")
        os.system("chcp 65001")

        form = resource_path1("libs/Ui/") + "*.ui"
        print(f"{form=}")
        # glob 모듈로 ui 확장자로된 파일만 추출
        self.uifileL = [f for f in glob(form)]
        self.cnt = len(self.uifileL)

        self.command = [("conda", "activate", "son-dev")]

        # ui 파일 개수 만큼 반복 하여 실행 명령어 생성
        for i in range(self.cnt):
            self.command.append(
                (
                    "pyuic5",
                    self.uifileL[i],
                    "-o",
                    self.uifileL[i].replace(".ui", ".py"),
                    "-x",
                )
            )

        print("setpath 완료")

    def getuipy(self):
        print("getuipy 시작")

        try:
            self.setpath()

            for x in self.command:
                print(x)
                self.popen = subprocess.Popen(
                    args=x,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    encoding="utf8",
                    shell=True,
                    text=True,
                )

                print("정상적으로 실행됨")
                (self.stdoutdata, self.stderrdata) = self.popen.communicate()
                print("결과1:", self.stdoutdata)
                print("***********")
                print("결과2:", self.stderrdata)

        except Exception as e:
            traceback.format_exc()
