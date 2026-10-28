from django.contrib import admin
from .models import OrderInfo


@admin.register(OrderInfo)
class OrderInfoAdmin(admin.ModelAdmin):
    # 展示订单核心信息
    list_display = ['order_sn', 'signer_name', 'signer_mobile', 'order_mount', 'pay_status', 'add_time']
    # 按支付状态过滤
    list_filter = ['pay_status']
    search_fields = ['order_sn', 'signer_name', 'signer_mobile']
    # 列表页允许直接修改状态
    list_editable = ['pay_status']

    # 🌟 核心：自定义批量发货动作 (对标任务书：订单发货处理)
    actions = ['ship_orders']

    @admin.action(description='🚀 一键发货 (变更为待收货)')
    def ship_orders(self, request, queryset):
        # 严格校验：只能给“待发货(unshipped)”或“已支付(paying)”的订单发货
        valid_orders = queryset.filter(pay_status__in=['unshipped', 'paying'])
        count = valid_orders.count()

        if count == 0:
            self.message_user(request, '选中的订单中没有满足发货条件的（需为待发货状态）', level='error')
            return

        valid_orders.update(pay_status='shipped')
        self.message_user(request, f'太棒了！成功为 {count} 个订单发货！')