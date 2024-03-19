
from django.contrib import admin
from django.urls import path

from blog.views import post_list, post_detail
from config.views import index

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index), # 경고 없을때 index 페이지로 연결
    path("posts/", post_list),
    path("posts/<int:post_id>/", post_detail),

]

# 유저가 업로드하는 정적 파일들을 이미지 링크와 연결하기
urlpatterns += static(
    # URL의 접두어가 MEDIA_URL일때는 정적 파일을 돌려준다.
    prefix = settings.MEDIA_URL,
    # 돌려줄 디렉토리는 MEDIA_ROOT 를 기준으로 한다.
    document_root = settings.MEDIA_ROOT,
)