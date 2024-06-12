from django.db import models

# Create your models here.

class Product(models.Model):

    name = models.CharField(max_length = 100)
    description = models.TextField()
    brand = models.CharField(max_length = 100)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits = 9, decimal_places = 2)
    available = models.BooleanField(default = True)
    creted_at = models.DateTimeField(auto_now_add = True)