from django.db import models
import moneyed
from djmoney.models.fields import MoneyField
# Create your models here.

class Bill(models.Model):
    name = models.CharField(max_length=100)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='GBP')
    