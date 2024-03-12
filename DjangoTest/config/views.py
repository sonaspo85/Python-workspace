from django.http import HttpResponse

# main(): 주문을 처리하는 직원, 즉, 직원이 HttpResponse 객체의 내용을 손님에게 보여준다.
def main(request): 
    # 브라우저에 텍스트를 전달하고 싶다면 HttpResponse객체를 리턴 한다.
    # HttpResponse는 Django가 돌려준 값을 브라우저가 읽을 수 있도록 적절한 처리를 해주는 역할을 한다.
    return HttpResponse('안녕하세요. son min chan 입니다.')