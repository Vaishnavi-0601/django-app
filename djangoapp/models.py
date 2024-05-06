from django.db import models

# Create your models here.
class Carlist(models.Model):
    name=models.CharField(max_length=10)
    description=models.CharField(max_length=200)
    active=models.BooleanField(default=False)