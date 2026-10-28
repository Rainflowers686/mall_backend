from django.contrib import admin
# 第一步：把我们刚刚在 models.py 里建好的三张表“请”过来
from .models import ShoppingCart, OrderInfo, OrderGoods

# 第二步：告诉 Django，把它们注册到后台管理网页中
admin.site.register(ShoppingCart)
admin.site.register(OrderInfo)
admin.site.register(OrderGoods)