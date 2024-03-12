echo build start!!!


set srcscript=main.py
set exename=CE_html_Converter
set exeiconF=libs/Ui/xxx.ico
set splashF=libs/Ui/Splash.png


set upxdir=C:\Users\SMC\anaconda3\envs\son-dev


rem set upxdir2=os.path.join(upxdir, 'Library/upx-4.2.1-win64')
set upxdir2=%upxdir%/Library/upx-4.2.1-win64



rem set root=C:\Users\SMC\anaconda3
set root=C:\Users\SMC\anaconda3\envs\son-dev

set projectDir=%cd%\AIR_Html_Converter\

call %root%\Scripts\activate.bat %root%

rem 현재 디렉토리를 프로젝트 디렉토리로 변경
call cd %projectDir%
echo %cd%

rem 전체 가상환경 목록 확인
call conda env list

rem 가상환경 활성화
call conda activate son-dev


rem 현재 버전 확인
FOR /F "tokens=*" %%g IN ('call python -V') do (SET aaa=%%g)
echo current_python_Version: %aaa%


rem exe 빌드 실행
pyinstaller --noconfirm ^
            --clean ^
            --upx-dir=%upxdir2% ^
            --upx-exclude=Qt*.dll ^
            --upx-exclude=PySide2/*.pyd ^
            --icon=%exeiconF% ^
            --add-data="./resource;./resource" ^
            --add-data="./libs/Ui;./libs/Ui" ^
            --splash=%splashF% ^
            --hidden-import=pyi_splash ^
            --name=%exename% ^
            --log-level=WARN ^
            --hidden-import=PyQt5.sip ^
            --hidden-import=darkdetect ^
            main.py

echo complete exe build!!


pause
