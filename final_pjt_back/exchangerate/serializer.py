from rest_framework import serializers
from .models import *

class ExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = '__all__'

class CountryFlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryFlag
        fields = '__all__'