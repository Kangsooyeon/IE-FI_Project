from django.db import models

# Create your models here.
class Location(models.Model):
    province = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    latitude = models.FloatField()
    longitude = models.FloatField()