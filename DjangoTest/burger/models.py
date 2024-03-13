from django.db import models


class burger(models.Model):
    # 문자열을 저장하는 CharField
    name = models.CharField(max_length=20)
    # 숫자를 저장하는 IntegerField
    price = models.IntegerField(default=0)
    caloris =models.IntegerField(default=0)