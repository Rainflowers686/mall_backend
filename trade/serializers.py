from rest_framework import serializers
from .models import ShoppingCart

class ShoppingCartSerializer(serializers.ModelSerializer):
    # 这三行是魔法：利用外键关系，直接把商品表里的名字、价格和图片拉取过来，设为只读
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2, read_only=True)
    product_image = serializers.ImageField(source='product.image', read_only=True)

    class Meta:
        model = ShoppingCart
        # 暴露给前端的字段，注意这里没有 user，因为 user 是后端自动绑定的
        fields = ['id', 'product', 'nums', 'is_selected', 'product_name', 'product_price', 'product_image']