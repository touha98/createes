from django.contrib import admin
from .models import Product
from internal.models import Costs


class ProductAdmin(admin.ModelAdmin):
    def total_orders(self, obj):
        total_products = obj.units_s + obj.units_m + obj.units_l + \
            obj.units_xl + obj.units_xxl + obj.units_3xl
        return total_products

    def sales(self, obj):
        return obj.price * self.total_orders(obj)

    def processing_cost(self, obj):
        costs = Costs.objects.filter(product__id=obj.id)
        total_cost = 0
        for cost in costs:
            total_cost += cost.amount
        return total_cost

    list_display = ('id', 'title', 'price', 'total_orders', 'sales',
                    'processing_cost', 'is_released', 'release_date', 'agent')
    list_display_links = ('id', 'title')
    list_filter = ('location', 'title')
    list_search = ('title', 'price', 'location')
    list_editable = ('is_released',)
    search_fields = ('title', 'description', 'price', 'color')
    list_per_page = 25


admin.site.register(Product, ProductAdmin)
