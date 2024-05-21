from django.urls import path
from . import views

app_name='news'

urlpatterns = [
    path('finance/', views.search_finance, name='search_finance'),
    path('economy/', views.search_economy, name='search_economy'),
    path('stock/', views.search_stock, name='search_stock'),
    path('coin/', views.search_coin, name='search_coin'),
]
