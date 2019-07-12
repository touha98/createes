from django.db import models
from datetime import datetime
from products.models import Product


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    roll = models.CharField(max_length=20, blank=True)
    dept = models.CharField(max_length=55, blank=True)
    txnid = models.CharField(max_length=30)
    size = models.CharField(max_length=3)
    units = models.IntegerField()
    payMethod = models.CharField(max_length=20)
    price = models.IntegerField()
    user_id = models.IntegerField()
    order_date = models.DateTimeField(default=datetime.now, blank=True)
    is_valid = models.BooleanField(default=0, blank=True)
    is_delivered = models.BooleanField(default=0, blank=True)

    def __str__(self):
        return self.name
