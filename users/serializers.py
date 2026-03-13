from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import serializers
from .models import Address, UserMessage

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        # 极其重要：告诉 DRF 前端不需要传 user_id，保护系统安全
        read_only_fields = ['user']
class UserMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMessage
        fields = '__all__'
        read_only_fields = ['user']
class UserRegSerializer(serializers.ModelSerializer):
    """用户注册序列化器"""
    class Meta:
        model = User
        fields = ['username', 'password']
        # 密码只能写入，不能在返回的数据里被看到，确保安全
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # ⚠️ 极其重要：必须用 create_user，它会自动对密码进行密文加密！
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user