from django.urls import path
from . import views

app_name='exchangerate'

urlpatterns = [
    path('', views.index, name='index'),
    path('save-ER/', views.save_ER, name='save_ER'),
    path('ER-graph/', views.ER_graph, name='ER_graph'),
]
