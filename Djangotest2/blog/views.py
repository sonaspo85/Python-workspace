from django.shortcuts import render
from blog.models import Post

def post_list(request):
    # 모든 Post 객체를 가진 요소를 추출
    posts = Post.objects.all()

    # 템플릿에 데이터를 전달하기 위해 딕셔너리 객체 생성,
    context = {
        'posts':posts,
    }

    # 3번째 인수로 Template에 전달할 데이터 할당
    return render(request, 'post_list.html', context)


def post_detail(request, post_id):
    return render(request, 'post_detail.html')
