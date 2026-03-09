from rest_framework import serializers
from .models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        # 极其重要：告诉 DRF 前端不需要传 user_id，保护系统安全
        read_only_fields = ['user']