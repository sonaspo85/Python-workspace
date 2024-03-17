
from django.shortcuts import render
from blog.models import Post

# localhost:8000 뒤에 아무런 경로도 추가되지 않았을때 보여줄 기본 인덱스 페이지
def index(request):
    # render() 함수를 사용하여 HTML 파일들을 브라우저로 돌려주기

    # 모든 Post 객체를 가진 요소를 추출
    posts = Post.objects.all()

    # 템플릿에 데이터를 전달하기 위해 딕셔너리 객체 생성,
    context = {
        'posts':posts,
    }

    # 3번째 인수로 Template에 전달할 데이터 할당
    return render(request, 'index.html', context)
