import os

from libs.controller.readCodesF import readCodeF


class setfileNlang:

    def __init__(self, srcpath):
        self.srcpath = srcpath



    def setDict(self):
        print('setDict 시작')

        files = os.listdir(self.srcpath)

        dic_map = {}

        for file in files:
            abspath = os.path.join(self.srcpath, file)
            print('abspath:', abspath)
            # filename = file.replace('.tmx', '')
            filename = os.path.splitext(file)[0]

            # codes.xml 에서 언어 목록 이 포함 된다면
            readCodef = readCodeF(filename)
            lang2 = readCodef.runReadCodes()

            dic_map[]
