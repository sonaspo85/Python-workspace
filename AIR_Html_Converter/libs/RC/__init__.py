__all__ = ["mainWindow", "langWindow"]

import getpass
import socket
import sys

from libs.Ui.convertUItpy import convertuiTpy
from libs.otherController.connectFTP import connectFTP
from setExePath import *

# import getpass

if not getattr(sys, "frozen", False):
    print("파이썬 실행 환경인 경우 ui 파일을 py파일로 변환!!")

    ct = convertuiTpy()
    ct.getuipy()
