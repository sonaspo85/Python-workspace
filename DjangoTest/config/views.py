from django.http import HttpResponse
from django.shortcuts import render
from burger.models import burger

# main(): 주문을 처리하는 직원, 즉, 직원이 HttpResponse 객체의 내용을 손님에게 보여준다.
def main(request): 
    # HTML 파일을 브라우저로 돌려주기 위해서 render() 함수 사용
    return render(request, 'main.html')

# 추가 페이지 구성하기
def sub_list1(request):
    bur = burger.objects.all()
    print('전체 버거 목록:', bur)


    # Template에 데이터를 전달할때는 딕셔너리 객체 형태로 전달하며
    # 관용적으로 딕셔너리 객체 이름은 context를 사용한다.
    context = {
        'burger':bur # burger라는 키 객체에 bur 속성값을 할당
    }
    
    # render 함수의 마지막 인수로 context 할당
    return render(request, 'aaa.html', context)

# 추가 페이지 구성하기2
def sub_list2(request):
    # 브라우저로부터 '?keyword=son'으로 키와 값을 값을 할당 받았다면
    # get('키객체') 함수로 키객체에 해당하는 값 객체를 추출할 수 있다.
    keyword = request.GET.get('keyword')
    print(keyword)


    # keyword 속성의 값이 None이 아닌 경우
    if keyword is not None:
        # name__contains: name 속성이 keyword 값을 포함하는 경우
        bur = burger.objects.filter(name__contains=keyword)

        # price__contains: price 속성이 keyword 값을 포함하는 경우
        # bur = burger.objects.filter(price__contains=keyword)
        print(f'{bur=}')

    # keyword 값이 주어지지 않아 None으로 할당된 경우
    else:
        # 빈 QuerySet 객체를 할당
        bur = burger.objects.none()

    # Template에 데이터를 전달하기 위해 context 딕셔너리 객체 선언후, render() 함수의 세번째 인수로 할당
    context = {
        'burger':bur,
    }
    return render(request, 'bbb.html', context)
