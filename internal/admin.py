from django.contrib import admin
from .models import Costs, Repository
from products.models import Product

class CostsAdmin(admin.ModelAdmin):
    list_display = ('cost_title', 'amount', 'product', 'time',)
    list_display_links = ('cost_title',)
    list_filter = ('product',)
    list_per_page = 25

class RepositoryAdmin(admin.ModelAdmin):
    def potential_value(self, obj):
        return obj.product.price * obj.units_manufactured

    list_display = ('__str__', 'units_manufactured', 'potential_value','batch_no', 'time',)
    list_display_links = ('__str__',)
    list_filter = ('product',)
    list_per_page = 25

admin.site.register(Costs, CostsAdmin)
admin.site.register(Repository, RepositoryAdmin)