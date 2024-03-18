from django.contrib import admin

from blog.models import Post, Comment


# 글을 작성하고 편집하는 Post 클래스에 대한 관리자 페이지 생성하기
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # 관리자 페이지에서 Post 정보를 확인할때 제목과 썸네일 이미지 필드 추가 하기
    list_display = ['title', 'thumbnail']


# Comment 클래스에 대한 관리자 페이지 생성
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass