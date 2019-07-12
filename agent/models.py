from django.db import models
from datetime import datetime
from accounts.models import User
from products.choices import location


class Agent(models.Model):
    userAcc = models.OneToOneField(
        User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True}, related_name="agent")
    photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    location = models.CharField(max_length=55, choices=location())
    phone = models.CharField(max_length=14)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.userAcc.first_name} {self.userAcc.last_name}"
