from django.db import models
from django.contrib.auth.models import User  # 引入 Django 自带的强力用户表


class Address(models.Model):
    """收货地址表"""
    # 这行最关键：用外键把地址和当前登录的用户死死绑定在一起
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="所属用户")

    receiver = models.CharField(max_length=20, verbose_name="收件人")
    phone = models.CharField(max_length=11, verbose_name="手机号")
    province = models.CharField(max_length=20, verbose_name="省份")
    city = models.CharField(max_length=20, verbose_name="城市")
    district = models.CharField(max_length=20, verbose_name="区/县")
    detail = models.CharField(max_length=100, verbose_name="详细地址")
    is_default = models.BooleanField(default=False, verbose_name="是否默认")  # 任务书要求的默认地址功能

    class Meta:
        verbose_name = "收货地址"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.user.username} - {self.receiver}"