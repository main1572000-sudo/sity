from django.db import models
from datetime import date
# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField()
    email = models.EmailField()
    date = models.DateField(default=date.today())
    # def __str__(self): 
    #     return self.name

class Product(models.Model):
    name = models.CharField(default='product??')
    price = models.IntegerField(default=00.00)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    #................................
    def __str__(self): 
        return self.name