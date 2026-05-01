from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=20,null=False)
    password = models.CharField()
    email = models.EmailField()
    # def __str__(self):
    #     return self.name