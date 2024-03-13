from django.http import HttpResponse
from django.shortcuts import render


# main(): 주문을 처리하는 직원, 즉, 직원이 HttpResponse 객체의 내용을 손님에게 보여준다.
def main(request): 
    # HTML 파일을 브라우저로 돌려주기 위해서 render() 함수 사용
    return render(request, 'main.html')

# 추가 페이지 구성하기
def sub_list1(request):
    return render(request, 'burger_list.html')