from django.shortcuts import render, redirect
from blog.models import Post, Comment


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

    # 브라우저로 전달받은 POST 방식의 데이터인 경우
    if request.method == 'POST':
        # 전달 받은 데이터는 'key=value' 의 형태로 전달 받는다.
        comment_content = request.POST['comment']

        # ojbects.create(): 객체 생성
        Comment.objects.create(
            post = post, # 현재 post 객체
            content = comment_content,

        )

    # Template 으로 데이터를 전달 하기 위해서는 딕셔너리 객체 타입으로 전달 해야 한다.
    context = {
        # 현재 Post 객체를 전달
        'post': post,
    }


    return render(request, 'post_detail.html', context)


def post_add(request):
    if request.method == 'POST':
        print('method POST 방식 입니다.')
        # 사용자가 POST 방식으로 전달한 데이터로 새로운 Post 객체 생성하기
        title = request.POST['title']
        print(f'{title=}') # title='나는 타이틀 입니다'

        content = request.POST['content']
        print(f'{content=}') # content='나는 내용 입니다.'

        # objects.create() : 새로운 Post 객체 생성
        post = Post.objects.create(
            title = title,
            content = content
        )

        # 새로운 Post 객체 생성후, 생성된 Post객체 페이지로 이동하기
        return redirect(f'/posts/{post.id}')
    else:
        print('method GET 방식 입니다.')

    return render(request, 'post_add.html')