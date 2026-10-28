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


import time
from random import Random
from django.db import transaction  # 极其强大的数据库事务护盾
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import ShoppingCart, OrderInfo, OrderGoods
from .serializers import ShoppingCartSerializer, OrderSerializer

# ... 之前写的 ShoppingCartViewSet 保持不动 ...

class OrderViewSet(viewsets.ModelViewSet):
    """订单一键结算 API"""
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        # 只能看自己的订单
        return OrderInfo.objects.filter(user=self.request.user)

    # 开启事务护盾：以下代码同生共死！
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 1. 找出当前用户购物车里【已勾选】的商品
        shop_carts = ShoppingCart.objects.filter(user=request.user, is_selected=True)
        if not shop_carts:
            return Response({"message": "购物车空空如也，无法结算哦"}, status=status.HTTP_400_BAD_REQUEST)

        # 2. 生成一个全球唯一的订单号 (当前时间 + 用户ID + 随机数)
        order_sn = f"{time.strftime('%Y%m%d%H%M%S')}{request.user.id}{Random().randint(10, 99)}"

        # 3. 算账：计算总金额
        order_mount = 0
        for cart in shop_carts:
            order_mount += cart.product.price * cart.nums

        # 4. 生成订单小票的“抬头” (保存到订单主表)
        order = serializer.save(user=request.user, order_sn=order_sn, order_mount=order_mount)

        # 5. 生成小票的“明细”，并扣库存、清空购物车
        for cart in shop_carts:
            OrderGoods.objects.create(
                order=order,
                product=cart.product,
                goods_num=cart.nums,
                price=cart.product.price
            )
            cart.product.stock -= cart.nums
            cart.product.save()

        # 6. 过河拆桥：清空已经结算的购物车！
        shop_carts.delete()

        return Response({
            "message": "下单成功！",
            "order_sn": order_sn,
            "total_price": order_mount
        }, status=status.HTTP_201_CREATED)