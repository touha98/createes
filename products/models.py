from django.db import models
from datetime import datetime
from agent.models import Agent
from .choices import location


class Product(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    price = models.IntegerField()
    color = models.TextField()

    bkash_no = models.CharField(max_length=11, blank=True)
    rocket_no = models.CharField(max_length=12, blank=True)

    s = models.BooleanField(default=True)
    m = models.BooleanField(default=True)
    l = models.BooleanField(default=True)
    xl = models.BooleanField(default=True)
    xxl = models.BooleanField(default=True)
    xxxl = models.BooleanField(default=True)

    units_s = models.IntegerField(default=0, blank=True)
    units_m = models.IntegerField(default=0, blank=True)
    units_l = models.IntegerField(default=0, blank=True)
    units_xl = models.IntegerField(default=0, blank=True)
    units_xxl = models.IntegerField(default=0, blank=True)
    units_3xl = models.IntegerField(default=0, blank=True)

    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_released = models.BooleanField(default=True)
    release_date = models.DateTimeField(default=datetime.now, blank=True)
    location = models.CharField(max_length=20, choices=location())

    def __str__(self):
        return self.title
