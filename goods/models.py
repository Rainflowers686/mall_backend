from django.db import models

class Category(models.Model):
    """商品分类表"""
    name = models.CharField(max_length=50, verbose_name="分类名称")

    class Meta:
        verbose_name = "商品分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Product(models.Model):
    """商品表"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="所属分类")
    name = models.CharField(max_length=100, verbose_name="商品名称")
    description = models.TextField(verbose_name="规格描述")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="价格")
    stock = models.IntegerField(default=0, verbose_name="库存显示")
    # 注意：因为这里用到了图片字段 ImageField，稍后我们需要装一个处理图片的库
    image = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name="商品图")
    is_hot = models.BooleanField(default=False, verbose_name="是否热门推荐")
    is_sale = models.BooleanField(default=True, verbose_name="是否上架")

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name