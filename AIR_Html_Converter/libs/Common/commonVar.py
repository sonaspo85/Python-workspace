# -*- coding: utf-8 -*-
import os
import shutil


class common:
    # 1. 프로젝트 디렉토리
    projectDir = ""
    srcPath = ""
    resourceDir = ""
    tempDir = ""
    xslsDir = ""
    zipDir = ""
    workISO = []  # 인터페이스에서 선택한 언어 코드 목록
    srcDirFullpath = []  # 각 src 디렉토리를 fullpath로 모음
    excelTemplsDir = ""
    typeTxt = ""
    radioTxt = ""
    langMap = {}
    nameNiso = {}
    isoNimgTuple = ()
    modelNum = ""
    currentISO = ""
    workingLngsL = []

    # def __init__(self):
    #     pass

    @classmethod
    def createNewDir(cls, dir):
        print("createNewDir 시작")

        try:
            if os.path.isdir(dir):
                print("common.zipDir 존재")
                # rmtree(): 디렉토리내 모든 중첩된 폴더 및 파일 삭제
                shutil.rmtree(dir)
                # 새롭게 생성
                os.makedirs(dir)
            else:
                os.makedirs(dir)

        except Exception as e:
            msg = "폴더 생성 실패"
            raise Exception(msg)
