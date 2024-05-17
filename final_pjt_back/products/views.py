from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import requests
from .serializer import *
from .models import *
# Create your views here.

API_KEY='b485257240fd200014c237dd7e0b6479'
BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'

@api_view(['GET'])
def deposit_list(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth' : API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1,
    }
    response = requests.get(URL, params=params).json()
    return JsonResponse(response)

@api_view(['GET'])
def saving_list(request):
    URL = BASE_URL + 'savingProductsSearch.json'
    params = {
        'auth' : API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1,
    }
    response = requests.get(URL, params=params).json()
    return JsonResponse(response)

@api_view(['GET'])
def save_deposit_products(reqeust):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth' : API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1,
    }
    response = requests.get(URL, params=params).json()

    baseList=response.get('result').get('baseList')
    optionList=response.get('result').get('optionList')

    for li in baseList:
        fin_prdt_cd = li.get('fin_prdt_cd')
        kor_co_nm = li.get('kor_co_nm')
        fin_prdt_nm = li.get('fin_prdt_nm')
        etc_note = li.get('etc_note')
        join_deny = li.get('join_deny')
        join_member = li.get('join_member')
        join_way = li.get('join_way')
        spcl_cnd = li.get('spcl_cnd')

        save_data = {
            'fin_prdt_cd':fin_prdt_cd,
            'kor_co_nm':kor_co_nm,
            'fin_prdt_nm':fin_prdt_nm,
            'etc_note':etc_note,
            'join_deny':join_deny,
            'join_member':join_member,
            'join_way':join_way,
            'spcl_cnd':spcl_cnd,
        }

        serializer = DepositProductsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save() 

    for li in optionList:
        fin_prdt_cd=li.get('fin_prdt_cd')
        intr_rate_type_nm=li.get('intr_rate_type_nm')
        intr_rate=li.get('intr_rate')
        intr_rate2=li.get('intr_rate2')
        save_trm=li.get('save_trm')

        product_instance = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)

        save_data = {
            'product': product_instance.pk,
            'fin_prdt_cd' : fin_prdt_cd,
            'intr_rate_type_nm' : intr_rate_type_nm,
            'intr_rate' : intr_rate,
            'intr_rate2' : intr_rate2,
            'save_trm' : save_trm,
        }

        serializer = DepositOptionsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return JsonResponse({'message':'저장완료'})


@api_view(['GET'])
def save_saving_products(reqeust):
    URL = BASE_URL + 'savingProductsSearch.json'
    params = {
        'auth' : API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1,
    }
    response = requests.get(URL, params=params).json()

    baseList=response.get('result').get('baseList')
    optionList=response.get('result').get('optionList')

    for li in baseList:
        fin_prdt_cd = li.get('fin_prdt_cd')
        kor_co_nm = li.get('kor_co_nm')
        fin_prdt_nm = li.get('fin_prdt_nm')
        etc_note = li.get('etc_note')
        join_deny = li.get('join_deny')
        join_member = li.get('join_member')
        join_way = li.get('join_way')
        spcl_cnd = li.get('spcl_cnd')

        save_data = {
            'fin_prdt_cd':fin_prdt_cd,
            'kor_co_nm':kor_co_nm,
            'fin_prdt_nm':fin_prdt_nm,
            'etc_note':etc_note,
            'join_deny':join_deny,
            'join_member':join_member,
            'join_way':join_way,
            'spcl_cnd':spcl_cnd,
        }

        serializer = SavingProductsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save() 

    for li in optionList:
        fin_prdt_cd=li.get('fin_prdt_cd')
        intr_rate_type_nm=li.get('intr_rate_type_nm')
        intr_rate=li.get('intr_rate')
        intr_rate2=li.get('intr_rate2')
        save_trm=li.get('save_trm')

        product_instance = get_object_or_404(SavingProducts, fin_prdt_cd=fin_prdt_cd)

        save_data = {
            'product': product_instance.pk,
            'fin_prdt_cd' : fin_prdt_cd,
            'intr_rate_type_nm' : intr_rate_type_nm,
            'intr_rate' : intr_rate,
            'intr_rate2' : intr_rate2,
            'save_trm' : save_trm,
        }

        serializer = SavingOptionsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return JsonResponse({'message':'저장완료'})



@api_view(['GET'])
def deposit_products(request):
    product_options = DepositOptions.objects.all()
    deposit_products_list = []

    for product_option in product_options:
        deposit_product = DepositProducts.objects.get(fin_prdt_cd=product_option.fin_prdt_cd)
        option_serializer = DepositOptionsSerializer(product_option)
        product_serializer = DepositProductsSerializer(deposit_product)
        deposit_products_list.append({
            'deposit_product': product_serializer.data,
            'options': option_serializer.data
        })
    return Response(deposit_products_list)

@api_view(['GET'])
def saving_products(reqeust):
    product_options = SavingOptions.objects.all()
    saving_products_list = []

    for product_option in product_options:
        saving_product = SavingProducts.objects.get(fin_prdt_cd=product_option.fin_prdt_cd)
        option_serializer = SavingOptionsSerializer(product_option)
        product_serializer = SavingProductsSerializer(saving_product)
        saving_products_list.append({
            'saving_product': product_serializer.data,
            'options': option_serializer.data
        })
    return Response(saving_products_list)


@api_view(['GET'])
def deposit_product(reqeust, id):
    depositProduct=DepositProducts.objects.filter(id=id)
    serializer = DepositProductsSerializer(depositProduct, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def saving_product(reqeust, id):
    savingProduct=SavingProducts.objects.filter(id=id)
    serializer = SavingProductsSerializer(savingProduct, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def deposit_product_options(reqeust, fin_prdt_cd):
    depositOption=DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(depositOption, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def saving_product_options(reqeust, fin_prdt_cd):
    savingOptions=SavingOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = SavingOptionsSerializer(savingOptions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def deposit_top_rate(reqeust):
    max_intr_rates = DepositOptions.objects.order_by('-intr_rate2')

    top_rate_data = []
    seen_products = set()

    for option in max_intr_rates:
        if option.fin_prdt_cd in seen_products:
            continue
        seen_products.add(option.fin_prdt_cd)

        product_detail = DepositProducts.objects.get(fin_prdt_cd=option.fin_prdt_cd)
        product_serializer = DepositProductsSerializer(product_detail)
        option_serializer = DepositOptionsSerializer(option)
        top_rate_data.append({
            'deposit_product': product_serializer.data,
            'option': option_serializer.data
        })

        if len(top_rate_data) >= 5:
            break
    return Response(top_rate_data)

@api_view(['GET'])
def saving_top_rate(reqeust):
    max_intr_rates = SavingOptions.objects.order_by('-intr_rate2')[:5]

    top_rate_data = []
    seen_products = set()
    
    for option in max_intr_rates:
        if option.fin_prdt_cd in seen_products:
            continue
        seen_products.add(option.fin_prdt_cd)

        product_detail = SavingProducts.objects.get(fin_prdt_cd=option.fin_prdt_cd)
        product_serializer = SavingProductsSerializer(product_detail)
        option_serializer = SavingOptionsSerializer(option)
        top_rate_data.append({
            'saving_product': product_serializer.data,
            'option': option_serializer.data
        })

        if len(top_rate_data) >= 5:
            break
    return Response(top_rate_data)