from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import requests
from .serializer import *
from .models import *

# Create your views here.

API_KEY='kHJV65CK0uTFRVoV0cdQ5xNGhnHZ742f'
BASE_URL='https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'

@api_view(['GET'])
def index(request):
    URL = BASE_URL
    params = {
        'authkey' : API_KEY,
        'data': 'AP01',
    }
    response = requests.get(URL, params=params).json()
    return Response(response)

@api_view(['GET'])
def save_ER(request):
    URL = BASE_URL
    params = {
        'authkey' : API_KEY,
        'data': 'AP01',
    }
    response = requests.get(URL, params=params).json()

    for er in response:
        cur_unit=er.get('cur_unit')
        #쉼표 제거하여 float형으로 변환
        ttb = float(er.get('ttb').replace(',', '')) if er.get('ttb') else None
        tts = float(er.get('tts').replace(',', '')) if er.get('tts') else None
        cur_nm=er.get('cur_nm')

        save_data={
            'cur_unit':cur_unit,
            'ttb':ttb,
            'tts':tts,
            'cur_nm':cur_nm,
        }

        serializer=ExchangeRateSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return JsonResponse({'message':'저장완료'})