from django.db import models

# Create your models here.
class Carlist(models.Model):
    name=models.CharField(max_length=10)
    description=models.CharField(max_length=200)
    active=models.BooleanField(default=False)
    chassisnumber=models.CharField(max_length=100, blank=True,null=True)
    price=models.DecimalField(max_digits=9,decimal_places=2,null=True)
