from django.db import models
from django.contrib.auth.models import User
from goods.models import Product  # 引入我们之前写好的商品表


class ShoppingCart(models.Model):
    """购物车表"""
    # 纽带1：绑定是谁的购物车
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="所属用户")
    # 纽带2：绑定购物车里是哪个商品
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="商品")

    nums = models.IntegerField(default=1, verbose_name="购买数量")
    is_selected = models.BooleanField(default=True, verbose_name="是否勾选")  # 满足任务书“支持多选”的要求

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name
        # ⚠️ 商业级联合约束：同一个用户，同一个商品，在购物车里只能有一条记录！
        # 如果用户再次点击“加入购物车”，后端应该是把 nums 数量 +1，而不是再多出一条重复的记录。
        unique_together = ("user", "product")

    def __str__(self):
        return f"{self.user.username} 的购物车 - {self.product.name}"