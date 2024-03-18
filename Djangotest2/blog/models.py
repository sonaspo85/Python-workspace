from django.db import models

class Post(models.Model):
    title = models.CharField('포스트 제목', max_length=100)
    content = models.TextField('포스트 내용')
    # 썸네일 이미지를 저장할 필드 추가
    thumbnail = models.ImageField('썸네일 이미지', upload_to='post', blank=True)

    # 일반적으로 테이블에 객체를 생성할 경우 객체 고유의 ID 값으로 반환 한다.
    # 객체를 좀더 쉽게 알아볼 수 있도록 객체 ID 대신 title 속성값으로 대체
    def __str__(self):
        return self.title


class Comment(models.Model):
    # ForeignKey 필드를 사용하여 1:N 연결이 되도록 구성해준다.
    # ForeignKey 필드는 첫번째 인수인 Post 테이블 Row의 ID 값을 갖는다.
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField('댓글 내용')

    def __str__(self):
        return f'{self.post.title} 의 댓글 (ID: {self.id})'