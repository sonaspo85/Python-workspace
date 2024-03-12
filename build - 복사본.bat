echo build start!!!

set root=C:\Users\SMC\anaconda3

set projectDir=%cd%\pythonProject\

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
pyinstaller --noconfirm --clean --onefile ^
            --icon="./ui/xxx.ico" ^
            --add-data="./sampleDB/DB.xml;./dbdir" ^
            --add-data="./ui;./ui" ^
            main2.py

echo complete exe build!!


pause
