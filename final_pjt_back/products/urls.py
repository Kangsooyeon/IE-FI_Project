from django.urls import path
from . import views

app_name='products'

urlpatterns = [
    path('deposit-list/', views.deposit_list, name='deposit_list'),
    path('saving-list/', views.saving_list, name='saving_list'),
    path('save-deposit-products/', views.save_deposit_products, name='save_deposit_products'),
    path('save-saving-products/', views.save_saving_products, name='save_saving_products'),
    path('deposit-products/', views.deposit_products, name='deposit_products'),
    path('saving-products/', views.saving_products, name='saving_products'),
    path('deposit-product/<int:id>/', views.deposit_product, name='deposit_product'),
    path('saving-product/<int:id>/', views.saving_product, name='saving_product'),
    path('deposit-product-options/<str:fin_prdt_cd>/', views.deposit_product_options, name='deposit_product_options'),
    path('saving-product-options/<str:fin_prdt_cd>/', views.saving_product_options, name='saving_product_options'),
    path('deposit-products/top_rate/', views.deposit_top_rate, name='deposit_top_rate'),
    path('saving-products/top_rate/', views.saving_top_rate, name='saving_top_rate'),

]
