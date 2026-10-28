from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# DRF 和 JWT 工具
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# 自动生成文档的神器工具
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# 引入咱们自己写的各个模块视图
from goods.views import ProductListAPIView
from users.views import AddressViewSet, UserMessageViewSet
from trade.views import ShoppingCartViewSet, OrderViewSet

# 🌟 必须先让 router 诞生！
router = DefaultRouter()

# 然后再把所有的增删改查视图挂载上去
router.register(r'api/addresses', AddressViewSet, basename='address')
router.register(r'api/messages', UserMessageViewSet, basename='messages')
router.register(r'api/cart', ShoppingCartViewSet, basename='cart')
router.register(r'api/orders', OrderViewSet, basename='order')

urlpatterns = [
                  # 基础与后台
                  path('admin/', admin.site.urls),

                  # 独立配置的接口
                  path('api/products/', ProductListAPIView.as_view()),
                  path('api/login/', TokenObtainPairView.as_view()),
                  path('api/token/refresh/', TokenRefreshView.as_view()),

                  # 🌟 Swagger UI 在线接口文档的专属网址
                  path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
                  path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
              ] + router.urls  # 把路由器生成的网址拼接到最后

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)