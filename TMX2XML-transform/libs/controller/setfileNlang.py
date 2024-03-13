import os

from libs.controller.readCodesF import readCodeF


class setfileNlang:

    def __init__(self, srcpath):
        self.srcpath = srcpath



    def setDict(self):
        print('setDict 시작')

        files = os.listdir(self.srcpath)

        for file in files:
            abspath = os.path.join(self.srcpath, file)
            # print('abspath:', abspath)
            filename = file.replace('.tmx', '')

            readCodef = readCodeF(filename)
            readCodef.runReadCodes()
