from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # 1. 列表页展示哪些字段
    list_display = ['id', 'name', 'price', 'is_sale']
    # 2. 右侧增加过滤器（可以按是否上架筛选）
    list_filter = ['is_sale']
    # 3. 顶部增加搜索框（可以搜商品名）
    search_fields = ['name']
    # 4. 在列表页可以直接编辑上下架状态，不用点进详情！
    list_editable = ['is_sale']

    # 🌟 核心：自定义批量操作动作 (对标任务书：商品上下架)
    actions = ['make_sale', 'make_offline']

    @admin.action(description='🔥 批量上架所选商品')
    def make_sale(self, request, queryset):
        rows_updated = queryset.update(is_sale=True)
        self.message_user(request, f'成功上架了 {rows_updated} 个商品！')

    @admin.action(description='❄️ 批量下架所选商品')
    def make_offline(self, request, queryset):
        rows_updated = queryset.update(is_sale=False)
        self.message_user(request, f'成功下架了 {rows_updated} 个商品！')