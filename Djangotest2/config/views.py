
from django.shortcuts import render

# localhost:8000 뒤에 아무런 경로도 추가되지 않았을때 보여줄 기본 인덱스 페이지
def index(request):
    # render() 함수를 사용하여 HTML 파일들을 브라우저로 돌려주기
    return render(request, 'index.html')
