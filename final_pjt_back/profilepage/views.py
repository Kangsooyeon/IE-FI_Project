from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404
from products.serializer import *
from datetime import datetime, date
from django.forms.models import model_to_dict
from itertools import groupby


# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def subscribed_deposit(request):
    subscribed_list=[]
    subscribed_products = SubscribedDepositProducts.objects.filter(user=request.user)
    for subscribed_product in subscribed_products:
        product=DepositProducts.objects.get(fin_prdt_cd=subscribed_product.deposit_option.fin_prdt_cd)
        product_serializer = DepositProductsSerializer(product)
        option_serializer = DepositOptionsSerializer(subscribed_product.deposit_option)
        subscribed_list.append({
            'id': subscribed_product.id,
            'deposit_product': product_serializer.data,
            'deposit_option': option_serializer.data,
            'sign_money': subscribed_product.sign_money,
            'mtrt_money': subscribed_product.mtrt_money
        })
    return Response(subscribed_list, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def subscribed_saving(request):
    subscribed_list=[]
    subscribed_products = SubscribedSavingProducts.objects.filter(user=request.user)
    for subscribed_product in subscribed_products:
        product=SavingProducts.objects.get(fin_prdt_cd=subscribed_product.saving_option.fin_prdt_cd)
        product_serializer = SavingProductsSerializer(product)
        option_serializer = SavingOptionsSerializer(subscribed_product.saving_option)
        subscribed_list.append({
            'id': subscribed_product.id,
            'saving_product': product_serializer.data,
            'saving_option': option_serializer.data,
            'sign_money': subscribed_product.sign_money,
            'mtrt_money': subscribed_product.mtrt_money
        })
    return Response(subscribed_list, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend_products(request):
    birth = datetime.strptime(request.user.birth, "%y%m%d").date()
    today = date.today()
    age = today.year - birth.year + 1
    asset = request.user.asset
    salary = request.user.salary
    total_asset = asset + salary
    main_bank = request.user.main_bank

    if age < 40:
        deposit_options = DepositOptions.objects.filter(save_trm__lte=12)
        saving_options = SavingOptions.objects.filter(save_trm__lte=12)
    elif age >= 40:
        deposit_options = DepositOptions.objects.filter(save_trm__gte=12)
        saving_options = SavingOptions.objects.filter(save_trm__gte=12)

    deposit_list = []
    for option in deposit_options:
        product = option.product
        max_limit = product.max_limit or 0
        if asset and max_limit < asset:
            option_dict = model_to_dict(option)
            option_dict['product'] = model_to_dict(option.product)
            deposit_list.append(option_dict)

    deposit_list.sort(key=lambda x: x['product']['fin_prdt_cd'])
    deposit_list = [max(list(group), key=lambda x: x['intr_rate2']) for key, group in groupby(deposit_list, key=lambda x: x['product']['fin_prdt_cd'])]
    deposit_list.sort(key=lambda x: x['intr_rate2'], reverse=True)

    saving_list = []
    for option in saving_options:
        product = option.product
        max_limit = product.max_limit or 0
        if (salary and max_limit < salary/12*0.6) or (asset and max_limit < asset/12*0.6):
            option_dict = model_to_dict(option)
            option_dict['product'] = model_to_dict(option.product)
            saving_list.append(option_dict)
    
    saving_list.sort(key=lambda x: x['product']['fin_prdt_cd'])
    saving_list = [max(list(group), key=lambda x: x['intr_rate2']) for key, group in groupby(saving_list, key=lambda x: x['product']['fin_prdt_cd'])]
    saving_list.sort(key=lambda x: x['intr_rate2'], reverse=True)

    dp_len=len(deposit_list)
    if total_asset < 50000000:
        if dp_len > 2:
            deposit_list = deposit_list[:2]
            saving_list = saving_list[:3]
        else:
            deposit_list = deposit_list[:dp_len]
            saving_list = saving_list[:5-dp_len]
            
        
    elif total_asset >= 50000000:
        if dp_len > 3:
            deposit_list = deposit_list[:3]
            saving_list = saving_list[:2]
        else:
            deposit_list = deposit_list[:dp_len]
            saving_list = saving_list[:5-dp_len]

    product_list = deposit_list + saving_list
    main_bank_products = [product for product in product_list if product['product']['kor_co_nm'] == main_bank]
    other_products = [product for product in product_list if product['product']['kor_co_nm'] != main_bank]
    product_list = main_bank_products + other_products

    data = {
        'age': age,
        'asset': asset,
        'salary': salary,
        'product_list': product_list,
    }
    return Response(data, status=status.HTTP_200_OK)
