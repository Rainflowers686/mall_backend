from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from goods.views import ProductListAPIView
# 新增：引入 JWT 提供好的登录发卡视图
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', ProductListAPIView.as_view()),

    # 新增：登录接口（前端用账号密码换取 JWT 门禁卡）
    path('api/login/', TokenObtainPairView.as_view()),
    # 新增：刷新接口（门禁卡过期了，用来换新卡的）
    path('api/token/refresh/', TokenRefreshView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)