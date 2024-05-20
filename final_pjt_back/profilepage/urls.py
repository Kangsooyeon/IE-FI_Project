from django.urls import path
from . import views

app_name='profilepage'

urlpatterns = [
    path('subscribed-deposit/', views.subscribed_deposit, name='subscribed_deposit'),
    path('subscribed-saving/', views.subscribed_saving, name='subscribed_saving'),
]
