from django.db import models

# Create your models here.
class ExchangeRate(models.Model):
    cur_unit = models.TextField(unique=True)
    ttb = models.FloatField()
    tts = models.FloatField()
    cur_nm = models.TextField()