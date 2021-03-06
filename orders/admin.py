from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'phone', 'adress',
                    'created', 'updated', 'finished', 'for_payment','paid',]
    list_filter = ['paid', 'created', 'updated', 'finished']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
