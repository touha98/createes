from django.db import models
from products.models import Product
from datetime import datetime

class Costs(models.Model):
    cost_title = models.CharField(max_length = 255)
    description = models.TextField(max_length=512, blank=True)
    amount  = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
    time = models.DateTimeField(blank=True, default = datetime.now)
    def __str__(self):
        return self.cost_title

class Repository(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    batch_no = models.IntegerField()
    units_manufactured  = models.IntegerField()
    note = models.CharField(max_length = 255, blank = True)
    time = models.DateTimeField(blank=True, default = datetime.now)
    def __str__(self):
        return (self.product.title + '_' + str(self.batch_no))
