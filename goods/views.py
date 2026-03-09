from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    """商品列表接口（支持过滤、搜索、排序）"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # 1. 配置你想使用哪些过滤引擎
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # 2. 精确筛选：允许前端通过“所属分类的ID”或“是否热门”来精确查找
    filterset_fields = ['category', 'is_hot']

    # 3. 模糊搜索：允许前端通过关键词去“商品名称”或“规格描述”里模糊搜索
    search_fields = ['name', 'description']

    # 4. 排序功能（赠品）：允许前端按价格从高到低或从低到高排序
    ordering_fields = ['price']