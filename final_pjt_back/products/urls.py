from django.urls import path
from . import views

app_name='products'

urlpatterns = [
    path('', views.index, name='index'),
    path('save-deposit-products/', views.save_deposit_products, name='save_deposit_products'),
    path('deposit-products/', views.deposit_products, name='deposit_products'),
    path('deposit-product/<int:id>/', views.deposit_product, name='deposit_product'),
    path('deposit-product-options/<str:fin_prdt_cd>/', views.deposit_product_options, name='deposit_product_options'),
    path('deposit-products/top_rate/', views.top_rate, name='top_rate'),

]
