import os.path

import PyInstaller.__main__
import pyinstaller_versionfile
import sys

srcscript = "main.py"
exename = "sand_mail"  # 출력 exe 파일 이름 지정
exeiconF = "ui/xxx.ico"  # exe 실행 프로그램 아이콘
splashF = "ui/Splash.png"

# exe 빌드시, 사이즈 줄이기
# sys.executable : 현재 실행 되고 있는 가상환경의 python.exe 경로를 반환 한다.
upxdir = os.path.dirname(sys.executable)
print("upxdir:", upxdir)

upxdir2 = os.path.join(upxdir, "Library/upx-4.2.1-win64")
adddata = []


pyinstaller_versionfile.create_versionfile(
    output_file="./fileinfo.txt",
    version="1.0",
    company_name="AST-GLOBAL",
    file_description="테스트 그룹메일 보내기 입니다.",
    internal_name="Simple App",
    legal_copyright="Copyright (c) AST-GLOBAL Technical comunication solution Foundation",
    original_filename="SimpleApp.exe",
    product_name="test productName",
    translations=[0, 1200],
)


PyInstaller.__main__.run(
    [
        "--noconfirm",
        "--clean",
        "--upx-dir=" + upxdir2,
        "--upx-exclude=Qt*.dll",
        "--upx-exclude=PySide2/*.pyd",
        "--icon=" + exeiconF,
        "--add-data=resource;resource",
        "--add-data=ui;ui",
        "--onefile",
        "--splash=" + splashF,
        # '--version-file=sampleDB/file_version_info.txt',
        "--version-file=./fileinfo.txt",
        "--noconsole",
        # '--hidden-import=pyi_splash',
        "--name=" + exename,
        srcscript,
    ]
)
