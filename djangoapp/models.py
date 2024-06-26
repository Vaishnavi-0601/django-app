from django.db import models
from rest_framework import serializers
from django.core.validators import MaxValueValidator,MinValueValidator

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
    showroom=models.ForeignKey('Showroomlist', on_delete=models.CASCADE,related_name="showrooms",null=True)

    def __str__(self):
        return self.name

class Showroomlist(models.Model):
    name=models.CharField(max_length=20)
    location=models.CharField(max_length=100)
    website=models.URLField(max_length=200)

    def __str__(self):
        return self.name

class Review(models.Model):
    rating=models.IntegerField(validators=[MaxValueValidator,MinValueValidator])
    comment=models.CharField(max_length=200,null=True)
    car=models.ForeignKey(Carlist,on_delete=models.CASCADE,related_name="Reviews",null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating)

