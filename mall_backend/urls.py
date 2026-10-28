from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from goods.views import ProductListAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# 新增：引入路由器和我们刚写的地址视图
from rest_framework.routers import DefaultRouter
from users.views import AddressViewSet
from trade.views import ShoppingCartViewSet # 新增：引入购物车视图

# 新增：让路由器自动帮我们生成增删改查的所有网址
router = DefaultRouter()
router.register(r'api/addresses', AddressViewSet, basename='address')
# 新增：让路由器帮我们生成购物车的网址
router.register(r'api/cart', ShoppingCartViewSet, basename='cart')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', ProductListAPIView.as_view()),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
] + router.urls  # 新增：把路由器生成的网址拼接到总网址里

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)