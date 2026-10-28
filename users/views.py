from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Address, UserMessage
from .serializers import AddressSerializer, UserMessageSerializer

class AddressViewSet(viewsets.ModelViewSet):
    """收货地址增删改查 API"""
    serializer_class = AddressSerializer
    # 权限控制：必须是带了正确 JWT Token 的用户才能访问
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # 安全隔离：查询时，只返回当前拿着门禁卡来访问的那个用户的地址
        return Address.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # 新增地址时：自动把当前访问的用户和这个新地址死死绑定
        serializer.save(user=self.request.user)

class UserMessageViewSet(viewsets.ModelViewSet):
    """在线客服留言 API"""
    permission_classes = [IsAuthenticated]
    serializer_class = UserMessageSerializer

    def get_queryset(self):
        # 只能看自己的留言
        return UserMessage.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # 自动绑定当前用户
        serializer.save(user=self.request.user)