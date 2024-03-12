import os.path

import PyInstaller.__main__
import pyinstaller_versionfile
import sys

srcscript = "main.py"
exename = "CE_html_Converter"  # 출력 exe 파일 이름 지정
exeiconF = "libs/Ui/xxx.ico"  # exe 실행 프로그램 아이콘
splashF = "libs/Ui/Splash.jpg"

# exe 빌드시, 사이즈 줄이기
# sys.executable : 현재 실행 되고 있는 가상환경의 python.exe 경로를 반환 한다.
upxdir = os.path.dirname(sys.executable)
print("upxdir:", upxdir)

upxdir2 = os.path.join(upxdir, "Library/upx-4.2.1-win64")

hiddenImport = ["pyi_splash", "PyQt5.sip", "darkdetect"]

pyinstaller_versionfile.create_versionfile(
    output_file="./fileinfo.txt",
    version="1.0",
    company_name="AST-TCS",
    file_description="CE HTML 변환 도구 입니다.",
    internal_name="Simple App",
    legal_copyright="Copyright (c) AST-TCS Technical Comunication Solution Foundation",
    original_filename=f"{exename}",
    product_name=f"{exename}",
)


PyInstaller.__main__.run(
    [
        "--noconfirm",
        "--clean",
        "--upx-dir=" + upxdir2,
        "--upx-exclude=Qt*.dll",
        "--upx-exclude=PySide2/*.pyd",
        "--icon=" + exeiconF,
        # '--add-data=resource;resource',
        "--add-data=libs/Ui;libs/Ui",
        "--onefile",
        # '--splash=' + splashF,
        "--noconsole",
        "--name=" + exename,
        "--log-level=WARN",
        "--hidden-import=pyi_splash",
        "--hidden-import=PyQt5.sip",
        "--hidden-import=darkdetect",
        # '--version-file=./fileinfo.txt',
        # '--hidden-import=saxonche',
        # '--hidden-import=nodekind',
        srcscript,
    ]
)
