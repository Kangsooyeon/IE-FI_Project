from django.db import models
from django.conf import settings


# Create your models here.

class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()
    mtrt_int = models.TextField()
    max_limit = models.IntegerField(default=0, null=True)


class DepositOptions(models.Model):
    product=models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    fin_prdt_cd=models.TextField()
    intr_rate_type_nm=models.CharField(max_length=100)
    intr_rate=models.FloatField()
    intr_rate2=models.FloatField()
    save_trm=models.IntegerField()

class SavingProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()
    mtrt_int = models.TextField()
    max_limit = models.IntegerField(default=0, null=True)

class SavingOptions(models.Model):
    product=models.ForeignKey(SavingProducts, on_delete=models.CASCADE)
    fin_prdt_cd=models.TextField()
    intr_rate_type_nm=models.CharField(max_length=100)
    intr_rate=models.FloatField()
    intr_rate2=models.FloatField()
    save_trm=models.IntegerField()


class SubscribedDepositProducts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    deposit_option = models.ForeignKey(DepositOptions, on_delete=models.CASCADE)
    sign_money = models.IntegerField()
    mtrt_money = models.IntegerField()

class SubscribedSavingProducts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    saving_option = models.ForeignKey(SavingOptions, on_delete=models.CASCADE)
    sign_money = models.IntegerField()
    mtrt_money = models.IntegerField()