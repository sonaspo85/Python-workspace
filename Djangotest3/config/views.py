from django.shortcuts import render

# 아무런 경로도 추가되지 않았을 경우 기본적으로 보여줄 인덱스 페이지를 구성한다.
def index(request):
    return render(request, 'index.html')