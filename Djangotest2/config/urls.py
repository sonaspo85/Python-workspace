
from django.contrib import admin
from django.urls import path

from blog.views import post_list
from config.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index), # 경고 없을때 index 페이지로 연결
    path("posts", post_list), # 경고 없을때 index 페이지로 연결

]
