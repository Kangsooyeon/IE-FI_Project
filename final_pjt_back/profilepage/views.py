from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404
from products.serializer import *

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
            'deposit_option': option_serializer.data
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
            'saving_option': option_serializer.data
        })
    return Response(subscribed_list, status=status.HTTP_200_OK)