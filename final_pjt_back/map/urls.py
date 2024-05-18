from django.urls import path
from . import views

app_name='map'

urlpatterns = [
    path('save-location/', views.save_location, name='save_location'),
    path('get-location/', views.get_location, name='get_location'),
]
