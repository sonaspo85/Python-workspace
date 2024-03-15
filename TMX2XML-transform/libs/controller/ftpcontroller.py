import ftplib
from pathlib import Path
from setExePath import *
import datetime as dt


HOST = '10.10.10.222'
PORT = 21
ID = 'tcs_ftp'
PW = 'ast1413'
ftp_path = '/tmx_2/json'


class ftpClass:

    def __init__(self, ftpfolder):
        self.ftpfolder = ftpfolder
        # print('self.ftpfolder:', self.ftpfolder)


        self.ftpclient = ftplib.FTP()
        self.ftpclient.encoding = 'utf-8'
        self.projectDir = Path(resource_path1('')).absolute().as_posix()
        self.files = []
        self.directories = []


    def runFTP(self):
        print('runFTP 시작')

        self.ftpclient.connect(HOST, PORT)
        self.ftpclient.login(ID, PW)

        welcome = self.ftpclient.getwelcome()
        print('welcome:', welcome)

        self.ftpclient.cwd(ftp_path)

        # 현재 디렉토리 반환
        wdir = self.ftpclient.pwd()
        print('wdir:', wdir)

        list = []
        self.ftpclient.dir(list.append)

        self.upLoadlocalTServer()

        self.txtupdateF()



    def txtupdateF(self):
        print('txtupdateF 시작')

        # 현재 시간 구하기
        date = dt.datetime.now()

        date2 = date.strftime('%Y-%m-%d %H:%M:%S')
        print(date2)

        # 데이터 생성
        txt = f'{self.ftpfolder} 업데이트: {date2}'
        print('self.ftpfolder:', self.ftpfolder)
        print(f'{txt=}')


        jsonpath = os.path.join(self.projectDir + '/json')
        txtF = jsonpath + '/update.txt'
        # print(f'{txtF=}')
        # 업데이트 내역 txt 파일 생성
        with open(txtF, 'w+', encoding='utf8') as f:
            f.write(txt)

        ftp_path2 = ftp_path + '/' + self.ftpfolder + '/update.txt'

        if os.path.isfile(txtF):
            with open(txtF, 'rb') as localF:
                self.ftpclient.storbinary('STOR ' + ftp_path2, localF)



    def upLoadlocalTServer(self):
        print('upLoadlocalTServer 시작')

        jsonpath = os.path.join(self.projectDir + '/json')
        files = os.listdir(jsonpath)


        for jsonF in files:
            filename = jsonF
            abspath = Path(jsonpath, jsonF).absolute().as_posix()
            ftp_path2 = ftp_path  + '/' + self.ftpfolder + '/' + filename

            print('ftp_path2:', ftp_path2)

            if os.path.isfile(abspath) and filename.lower().endswith('.json'):
                with open(abspath, 'rb') as localF:
                    self.ftpclient.storbinary('STOR ' + ftp_path2, localF)


