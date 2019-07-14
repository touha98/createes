from django.contrib import admin
from .models import Order
from products.models import Product
from agent.models import Agent
from django.core.mail import send_mail
from django.db.models import F


class OrderAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        agent = Agent.objects.get(userAcc__id=request.user.id)
        query = super(OrderAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            filtered_query = query.filter(
                product__location=agent.location)
            return filtered_query
        return query

    list_editable = ('is_valid', 'is_delivered',)
    list_display = ('id', 'name', 'payMethod', 'txnid', 'product', 'size',
                    'units', 'phone', 'is_valid', 'is_delivered', 'order_date')
    list_display_links = ('id', 'name',)

    search_fields = ('name', 'email', 'size', 'phone', 'product__title')
    list_filter = ('product__title', 'size', 'is_valid', 'is_delivered')
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        if 'is_valid' in form.changed_data:
            if obj.is_valid:
                send_mail(
                    "Your order is approved!",
                    f"Your order for {obj.product.title} has been approved and will be delivered soon!",
                    'createes',
                    [obj.email],
                    fail_silently=True
                )
                if obj.size == 's':
                    Product.objects.filter(id=obj.product.id).update(
                        units_s=F('units_s') + obj.units)
                elif obj.size == 'm':
                    Product.objects.filter(id=obj.product.id).update(
                        units_m=F('units_m') + obj.units)
                elif obj.size == 'l':
                    Product.objects.filter(id=obj.product.id).update(
                        units_l=F('units_l') + obj.units)
                elif obj.size == 'xl':
                    Product.objects.filter(id=obj.product.id).update(
                        units_xl=F('units_xl') + obj.units)
                elif obj.size == 'xxl':
                    Product.objects.filter(id=obj.product.id).update(
                        units_xxl=F('units_xxl') + obj.units)
                else:
                    Product.objects.filter(id=obj.product.id).update(
                        units_3xl=F('units_3xl') + obj.units)

        super().save_model(request, obj, form, change)


admin.site.register(Order, OrderAdmin)
