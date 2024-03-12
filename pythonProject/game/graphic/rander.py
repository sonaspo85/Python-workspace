# 첫번째 방법 - 도드 연산자를 사용하여 다른 패키지내 모듈 찾아가기
from game.sound.echo import *

# 두번째 방법 - 상대 경로접근 방식을 사용하여 다른 패키지내 모듈 찾아가기
# from ..sound.echo import *


def render_test():
    print("render_test 함수 호출")
    echo()
