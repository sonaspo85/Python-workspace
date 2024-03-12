import traceback

from RC.mainWindow import *
from setExePath import *

#######################################################################
# 첫번째 방법 - 단일 exe로 패키징할 경우 패키지 내부의 ui 파일로 접근 하기
form = resource_path1("ui/root.ui")


if __name__ == "__main__":
    try:
        # exe 응용 프로그램 시작시 출력되었던 스플래시 화면 닫기
        # exe 실행 환경에서 실행 되었다면, pyi_splash를 import 하고 close()함수로 닫아주기
        # pyi_splash 모듈은 패키지 관리자로 설치 할 수 없으며, pyinstaller의 일부이기 때문에,
        # exe 빌드시에만 임포트 되어야 한다.
        if getattr(sys, "frozen", False):
            import pyi_splash

            pyi_splash.close()

        # QApplicationi : 응용 프로그램을 실행 시켜주는 클래스
        # sys.argv : 현재 소스 코드(main2.py)가 위치하고 있는 경로를 담고 있는 리스트를 클래스의 생성자로 전달
        app = QApplication(sys.argv)

        # windowClass 클래스를 인스턴스 객체로 생성
        mainWindow = MainWindow()

        mainWindow.show()

        # 프로그램을 작동시키는 코드
        app.exec_()

    except Exception as e:
        print(traceback.format_exc())
