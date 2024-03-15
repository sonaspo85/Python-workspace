import ftplib
from pathlib import Path
from setExePath import *


HOST = '10.10.10.222'
PORT = 21
ID = 'tcs_ftp'
PW = 'ast1413'
ftp_path = '/tmx_2/json/son'


class ftpClass:

    def __init__(self, ftpfolder):
        self.ftpfolder = ftpfolder

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