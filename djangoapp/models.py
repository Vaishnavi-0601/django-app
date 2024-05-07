from django.db import models
from rest_framework import serializers

def alphanumberic(value):
    if not str(value).isalnum():
        raise serializers.ValidationError("enter alphanumberic value")
# Create your models here.
class Carlist(models.Model):
    name=models.CharField(max_length=10)
    description=models.CharField(max_length=200)
    active=models.BooleanField(default=False)
    chassisnumber=models.CharField(max_length=100, blank=True,null=True,validators=[alphanumberic])
    price=models.DecimalField(max_digits=9,decimal_places=2,null=True)
