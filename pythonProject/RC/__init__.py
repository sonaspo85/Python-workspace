__all__ = ["mainWindow", "subWindows", "file_lineEdit"]

from convertUItpy import *


if not getattr(sys, "frozen", False):
    print("파이썬 실행 환경인 경우 ui 파일을 py 파일로 변환!!")
    getuipy()
