from django.db import models
from django.contrib.auth.models import User
from goods.models import Product

class ShoppingCart(models.Model):
    """购物车表"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="所属用户")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="商品")
    nums = models.IntegerField(default=1, verbose_name="购买数量")
    is_selected = models.BooleanField(default=True, verbose_name="是否勾选")

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name
        unique_together = ("user", "product")

    def __str__(self):
        return f"{self.user.username} 的购物车 - {self.product.name}"


class OrderInfo(models.Model):
    """订单主表：相当于小票的抬头和结尾"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="下单用户")
    order_sn = models.CharField(max_length=30, null=True, blank=True, unique=True, verbose_name="订单编号")
    # 🌟 补丁 3：完美对标任务书的订单状态机
    pay_status = models.CharField(
        choices=(
            ("paying", "待支付"),
            ("shipping", "待发货"),
            ("receiving", "待收货"),
            ("success", "已完成"),
            ("closed", "已取消")
        ),
        default="paying", max_length=30, verbose_name="订单状态"
    )
    order_mount = models.FloatField(default=0.0, verbose_name="订单总金额")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="下单时间")

    address = models.CharField(max_length=100, default="", verbose_name="收货详细地址")
    signer_name = models.CharField(max_length=20, default="", verbose_name="签收人")
    signer_mobile = models.CharField(max_length=11, verbose_name="联系电话")

    class Meta:
        verbose_name = "订单信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)


class OrderGoods(models.Model):
    """订单商品详情表：相当于小票上列出的一件件商品"""
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, related_name="goods", verbose_name="所属订单")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="商品")
    goods_num = models.IntegerField(default=0, verbose_name="购买数量")
    price = models.FloatField(default=0.0, verbose_name="商品单价")

    class Meta:
        verbose_name = "订单商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)