from multiprocessing import Process


# Process 를 상속 받는 서브 클래스 선언
class subp1(Process):
    def __init__(self, string):
        Process.__init__(self)
        self.string = string

    # 서브 클래스 선언시 반드시 run() 함수 재정의
    def run(self):
        print("self.string:", self.string)
