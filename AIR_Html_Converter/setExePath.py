# -*- coding: utf8 -*-
import os
import sys


# 첫번째 방법 - 단일 exe로 패키징할 경우 패키지 내부의 ui 파일로 접근 하기
# pyinstaller 또는 개발 환경에 따라 절대 경로 추출하기
def resource_path1(relative_path):
    # getattr() : pyinstaller 으로 패키징 상태인지 아닌지 판별할 수 있는 함수이다.
    if getattr(sys, "frozen", False):
        # pyinstaller는 파일을 실행 파일로 패키징 할때 pyinstaller 부트로더는 임시 python 환경을 만들고 임시 _MEIPASS 라는 폴더를 생성 하고, 해당 임시 폴더에 패키지의 복사본 압축을 풀고 작업을 진행 하게 된다.
        # 그렇기 때문에, 실제 exe 파일이 위치한 경로가 아닌 임시 생성한 복사본의 경로를 가리키게 된다.
        # 실제로 exe 단일 파일로 패키징 후, 실행 하면 sys._MEIPASS의 반환 값은 "C:/Users/sonas/AppData/Local/Temp/_MEI109162/" 를 반환 한다.
        application_path = sys._MEIPASS

        # exe 실행시 시작 화면 출력하기
        # openSplash()
        # import pyi_splash
        # pyi_splash.update_text('UI Updata...')

    else:
        application_path = os.path.dirname(__file__)

    print(os.path.join(application_path, relative_path))
    return os.path.join(application_path, relative_path)


###########################################################################
# 두번째 방법 - exe로 패키징할 경우 패키지 내부가 아닌 외부 디렉토리의 ui 파일로 접근 하기
# # pyinstaller 또는 개발 환경에 따라 절대 경로 추출하기
def resource_path2(relative_path):
    # getattr() : pyinstaller로 패키징이 된 상태인지 아닌지를 판별할 수 있는 함수이다.
    if getattr(sys, "frozen", False):
        # sys.executable : 현재 실행환경이 패키징된 exe인 경우 실행 중인 exe 의 경로를 반환 한다.
        application_path = os.path.dirname(sys.executable)

    else:  # 파이썬 실행 환경에서 실행한 경우
        # __file__ : 현재 수행중인 코드를 담고 있는 파일의 경로를 반환 한다.
        application_path = os.path.dirname(__file__)

    print(os.path.join(application_path, relative_path))
    return os.path.join(application_path, relative_path)

    # _ui_path = os.path.join(RELATIVE_PATH, "uiPath/root.ui")  # Update this as needed
    # return _ui_path


###########################################################################
# 세번째 방법 - 단일 exe로 패키징할 경우 패키지 내부의 ui 파일로 접근 하기
def resource_path3(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def openSplash():
    print("openSplash 시작")

    import pyi_splash

    pyi_splash.update_text("UI Updata...")
