from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
# Create your models here.

class Base(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(Base):
    cat_name = models.CharField(max_length=255, unique=True, default="General")


class Product(Base):
    prod_name = models.CharField(max_length=255,null=False,unique=True)
    description = models.CharField(max_length=255,null=True)
    image = models.CharField(max_length=255,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

