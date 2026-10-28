from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import ShoppingCart
from .serializers import ShoppingCartSerializer


class ShoppingCartViewSet(viewsets.ModelViewSet):
    """购物车增删改查 API"""
    permission_classes = [IsAuthenticated]  # 必须拿着 JWT 门禁卡才能进
    serializer_class = ShoppingCartSerializer

    def get_queryset(self):
        # 核心安全：只能看到当前登录用户自己的购物车
        return ShoppingCart.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        # 拦截前端发来的“加入购物车”请求
        product_id = request.data.get('product')
        # 如果前端没传数量，默认就是加 1 个
        nums = int(request.data.get('nums', 1))

        # 去数据库里找找看，这个用户的购物车里是不是已经有这个商品了？
        cart_item = ShoppingCart.objects.filter(user=request.user, product_id=product_id).first()

        if cart_item:
            # 如果有，数量累加并保存！
            cart_item.nums += nums
            cart_item.save()
            # 重新翻译成 JSON 返回给前端
            serializer = self.get_serializer(cart_item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # 如果没有，走原本正常的创建流程
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)