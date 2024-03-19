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
    # Post 객체의 id 값이 post_id 의 정수값과 같은 Post 객체
    post = Post.objects.get(id=post_id)
    print(f'{post=}') # post=<Post: 테스트글 2>


    # Template에 데이터 전달하기, Template으로 데이터를 전달하기 위해서는 딕셔너리 객체로 전달해야 한다.
    # 관용적으로 context 이름으로 사용한다.
    context = {
        'post_id':post_id,
        'post':post,
    }

    return render(request, 'post_detail.html', context)
