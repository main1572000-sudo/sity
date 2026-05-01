from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=20,default='name')
    password = models.CharField(default='password')
    email = models.EmailField(default='email')
    # def __str__(self):
    #     return self.name