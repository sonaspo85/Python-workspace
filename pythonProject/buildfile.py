import os.path

import PyInstaller.__main__
import pyinstaller_versionfile
import sys

srcscript = "main2.py"
exename = "test"  # 출력 exe 파일 이름 지정
exeiconF = "ui/xxx.ico"  # exe 실행 프로그램 아이콘
splashF = "sampleDB/Splash.png"

# exe 빌드시, 사이즈 줄이기
# sys.executable : 현재 실행 되고 있는 가상환경의 python.exe 경로를 반환 한다.
upxdir = os.path.dirname(sys.executable)
upxdir2 = os.path.join(upxdir, "Library/upx-4.2.1-win64")
adddata = []


pyinstaller_versionfile.create_versionfile(
    output_file="sampleDB/fileinfo.txt",
    version="5.4.0.1",
    company_name="AST-GLOBAL",
    file_description="테스트용 정보 입니다.",
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
        "--add-data=sampleDB;sampleDB",
        "--add-data=ui;ui",
        "--onefile",
        "--splash=" + splashF,
        # '--version-file=sampleDB/file_version_info.txt',
        "--version-file=sampleDB/fileinfo.txt",
        # '--noconsole',
        # '--hidden-import=pyi_splash',
        "--name=" + exename,
        srcscript,
    ]
)
