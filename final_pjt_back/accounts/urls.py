from django.urls import path, include
from .views import *
from rest_framework import urls

app_name='accounts'

urlpatterns = [
    path('signup/', UserCreate.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('update/', UserUpdateView.as_view(), name='update'),
    path('api-auth/', include('rest_framework.urls')),

]