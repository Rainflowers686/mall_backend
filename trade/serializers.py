from rest_framework import serializers
from .models import ShoppingCart, OrderInfo

# 引入你的商品序列化器
from goods.serializers import ProductSerializer


class ShoppingCartSerializer(serializers.ModelSerializer):
    # 🌟 核心魔法：在读取购物车时，自动把关联的 product 展开成完整的字典
    # 这样前端就能直接通过 item.product.name 和 item.product.image 拿到数据
    product = ProductSerializer(read_only=True)

    # 🌟 这一行是为了保证你“加入购物车”的 POST 请求依然能用商品 ID 提交
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = ShoppingCart
        # 完美融合：保留了你的 is_selected，并使用了更优雅的 product 嵌套结构
        fields = ['id', 'product', 'product_id', 'nums', 'is_selected']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderInfo
        # 前端只需要传这三个字段，别的我们后端统统自己生成
        fields = ['address', 'signer_name', 'signer_mobile']