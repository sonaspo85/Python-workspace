"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from config.views import *

urlpatterns = [
    path("admin/", admin.site.urls), # 관리자 페이지
    path('', index), # 기본적으로 보유줄 페이지
]

# 유저가 업로드한 정적 파일들을 불러오기 위해서는 별도의 설정을 추가적으로 해주어야 한다.
urlpatterns +=  static(
    # URL의 접두어가 MEDIA_URL 일때는 정적 파일을 돌려준다.
    prefix = settings.MEDIA_URL,
    # 돌려줄 디렉토리는 MEDIA_ROOT 를 기준으로 한다.
    document_root = settings.MEDIA_ROOT,

)