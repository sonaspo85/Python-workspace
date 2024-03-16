from django.db import models


class burger(models.Model):
    # 문자열을 저장하는 CharField
    name = models.CharField(max_length=20)
    # 숫자를 저장하는 IntegerField
    price = models.IntegerField(default=0)
    calories =models.IntegerField(default=0)


    # str: 클래스 객체 자체의 내용을 출력하고 싶을때 사용
    def __str__(self):
        # 관리자 페이지에서 버거 항목을 추가하였을 경우 burger object 라는 사용자가 알아보는데 도움이 되지않는 이름으로 작성되어 있을 것이다.
        # 이름을 좀더 명확히 하기 위해 name 필드의 버거 이름을 출력하도록 설정 한다.
        return self.name