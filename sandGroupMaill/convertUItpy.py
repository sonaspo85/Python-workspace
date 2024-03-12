# -*- coding:utf8 -*-
import subprocess
from setExePath import *

command = ""


def setpath():
    print("setpath 시작")

    os.system("chcp 65001")

    form = resource_path1("ui/root.ui")
    print(f"{form=}")

    # uipath = "G:/MS-Drive/OneDrive - UOU/WORK/Workspace/WORK/PYTHON/python-workspace/pythonProject/ui/root.ui"
    uipath = form

    # split() : 경로와 파일명으로 분리하여 튜플 타입으로 반환 한다.
    uidir, uiname = os.path.split(uipath)
    # print(f'{uidir=}')
    # print(f'{uiname=}')

    uiname = uiname.replace(".ui", ".py")

    # 새롭게 생성될 ui.py 절대 경로생성
    newuipath = os.path.join(uidir, uiname)
    print(f"{newuipath=}")

    # subprocess 모듈의 popen 객체의 args 파라미터로 사용될 명령어 작성하기
    global command
    command = [
        ("conda", "activate", "son-dev"),
        ("python", "-V"),
        ("pyuic5", uipath, "-o", newuipath, "-x"),
    ]


def getuipy():
    print("getuipy 시작")

    try:
        # ui 파일 전체 경로 및 새롭게 생성될 ui.py 파일의 저장 경로 설정
        setpath()
        # popen = subprocess.Popen(args=command, stdin=subprocess.PIPE,
        # stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf8',
        # shell=True, text=True, env={'Path': 'C:/Users/sonas/anaconda3;C:/Users/sonas/anaconda3/Scripts'},
        # cwd='C:/Users/sonas/anaconda3/Scripts')

        for x in command:
            # print('x:', x)
            popen = subprocess.Popen(
                args=x,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                encoding="utf8",
                shell=True,
                text=True,
            )

            print("정상적으로 실행됨")
            # communicate() : 자식 프로세스가 종료될 때까지 대기 하며, 종료시 결과값을읽어 온다.
            # communicate() 는 파이썬 스트립트환경과 별개로 실행 된다.
            (stdoutdata, stderrdata) = popen.communicate()
            print("결과1:", stdoutdata)
            print("***********")
            print("결과2:", stderrdata)

    except Exception as e:
        print("에러 발생")

    finally:
        print("finally 블록 실행됨, 종료하기")
