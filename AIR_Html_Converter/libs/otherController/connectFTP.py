# -*- coding: utf8 -*-
import ftplib
import os.path
from pathlib import Path
from lxml import etree as et

from libs.Common.commonVar import common


class connectFTP(common):
    def __init__(self):
        pass

    def read_workinglngs(self):
        print("read_workinglngs 시작")

        try:
            # 1. docInfo.xml 파일 경로

            self.docinfoF = Path(self.resourceDir, "docInfo.xml")
            self.parser = et.XMLParser(ns_clean=True, encoding="utf8", recover=True)
            self.doc = et.parse(self.docinfoF, self.parser)
            # 2. root 태그 접근
            self.root = self.doc.getroot()

            for child in self.root.findall(".//item[@id='workinglngs']"):
                self.isocode = child.get("isocode")
                self.outputpath = child.get("outputpath")
                print("self.outputpath:", self.outputpath)
                self.ftpdir = (
                    "/tcs/confidential/CE-HTML-Converter/Templates/html_templates"
                )
                self.runFTP(self.ftpdir, self.outputpath)
                self.workingLngsL.append(child)

        except Exception as e:
            raise

    def runFTP(self, ftpdir, localoutDir):
        print("runFTP 시작")

        try:
            self.login()

            # 1. FTP 디렉토리 변경
            self.chgdir = ftpdir

            # 2. dir() 함수로 디렉토리내 탐색한 모든 요소들을 리스트 타입으로 저장
            files, directories = self.get_list_ftp(self.chgdir)

            # 3. 로컬 드라이브에 디렉토리 생성하기
            self.createLocalFolder(directories, localoutDir)
            # 로컬로 파일 다운로드
            self.DownServerTlocal(files, localoutDir)

            files.clear()
            directories.clear()

        except Exception as e:
            raise

        else:
            print("다운로드 완료")
            self.ftpobj.close()  # 서버 닫기

    def DownServerTlocal(self, files, outputpath):
        print("DownServerTlocal 시작")

        try:
            for file in files:
                # local_abspath = self.srcDir + '/test' + file.replace(self.chgdir, '')
                self.local_Filepath = outputpath + file.replace(self.chgdir, "")

                with open(self.local_Filepath, "wb") as localfile:
                    # retrbinary() : 바이너리 전송 모드로 파일을 복사 시켜 온다.
                    # 서버로 부터 파일을 다운로드하는 'RETR' 명령을 사용
                    self.ftpobj.retrbinary(f"RETR {file}", localfile.write)

                # 콘솔 출력
                # print('다운로드 파일:' + file)

        except Exception as e:
            msg = "로컬 디렉토리에 파일 복사 실패"
            raise Exception(msg)

    def createLocalFolder(self, directories, outputpath):
        print("createLocalFolder 시작")

        try:
            for folder in directories:
                # 상대 경로를 절대 경로로 변경
                self.local_Dirpath = outputpath + "/" + folder
                # print(f'{self.local_Dirpath=}')

                # 디렉토리가 존재하지 않으면 생성
                if not os.path.isdir(self.local_Dirpath):
                    os.makedirs(self.local_Dirpath)

        except Exception as e:
            msg = "로컬 PC에 폴더 생성 실패"
            raise Exception(msg)

    def get_list_ftp(self, cwd, files=[], directories=[]):
        print("get_list_ftp 시작")

        self.data = []

        # 1. 디렉토리 위치 변경하기
        self.ftpobj.cwd(cwd)
        # 2. 디렉토리 하위의 목록 추출하기, 바로 하위의 목록만 추출 가능
        self.ftpobj.dir(self.data.append)
        # 3. 반복문으로 탐색
        for item in self.data:
            # print(files)
            # rfind() : 문자열을 검색하는데 오른쪽 부터 인덱싱된 위치값을 찾아 반환
            # rfind() 함수로 찾는 이유는 files 변수의 반환 값이
            # files='drwxrwxrwx   1 sonminchan users              34 Feb 26 08:41 contents' 로출력되기 때문이다.
            self.pos = item.rfind(" ")
            # ftp 초기 경로 + 파일 이름(디렉토리 이름) 절대 경로로 만들기
            self.ftp_abpath = cwd + "/" + item[self.pos + 1 :]

            self.ftp_abpath2 = self.ftp_abpath.replace(self.chgdir, "")

            if item.find("drwxrwxrwx") > -1:
                # print('폴더임:', self.ftp_abpath)
                # self.ftp_abpath2 = self.ftp_abpath.replace(self.chgdir, '')
                directories.append(self.ftp_abpath2)
                # 하위 디렉토리를 탐색하기 위해 절대 경로 생성하기
                subdirs = self.ftp_abpath + "/"
                # 재귀적 함수로 하위 디렉토리 탐색
                self.get_list_ftp(subdirs, files, directories)

            else:
                # print('파일임:', item)
                # print(f'{self.ftp_abpath=}')
                files.append(self.ftp_abpath)

        # 파일과 디렉토리 리스트를 반환
        return files, directories

    def login(self):
        print("login 시작")

        self.HOST = "10.10.10.2"
        self.PORT = 21
        self.ID = "sonminchan"
        self.PW = "astkorea1234"

        try:
            # 1. ftp 객체 생성
            self.ftpobj = ftplib.FTP()
            self.ftpobj.encoding = "utf8"
            # 2. 포트번호 할당
            self.ftpobj.connect(self.HOST, self.PORT)
            # 3. FTP 서버 접속을 위한 ID, PW 입력
            self.ftpobj.login(self.ID, self.PW)
            # 접속 메시지 출력
            # self.getmsg = self.ftpobj.getwelcome()

        except Exception as e:
            self.msg = "FTP 접속 거부"
            raise Exception(self.msg)

    def uploadF(self, ftppath, excelF):
        print("uploadF 시작")

        self.login()

        # 디렉토리 위치 변경
        self.ftpobj.cwd(ftppath)
        ftppath2 = ftppath + "/template1.xlsx"

        with open(excelF, "rb") as localF:
            self.ftpobj.storbinary(f"STOR {ftppath2}", localF)
