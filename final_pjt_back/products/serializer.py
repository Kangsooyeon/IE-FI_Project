from rest_framework import serializers
from .models import *


class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'

class DepositOptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = DepositOptions
        fields = '__all__'


class SavingProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'

class SavingOptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SavingOptions
        fields = '__all__'


class SubscribedDepositProductsSerializer(serializers.ModelSerializer):
    deposit_option = DepositOptionsSerializer(read_only=True)
    class Meta:
        model = SubscribedDepositProducts
        fields = '__all__'

class SubscribedSavingProductsSerializer(serializers.ModelSerializer):
    saving_option = SavingOptionsSerializer(read_only=True)
    class Meta:
        model = SubscribedSavingProducts
        fields = '__all__'

