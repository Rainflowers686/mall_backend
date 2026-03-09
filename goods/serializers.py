from rest_framework import serializers
from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    # 这一行很贴心：默认情况下分类只会显示一个数字 ID，这行代码能帮前端直接拿到分类的具体中文名称
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'  # 意思是把模型里的所有字段都翻译成 JSON