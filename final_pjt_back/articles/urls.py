from django.urls import path
from . import views

app_name='articles'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('create/', views.article_create, name='article_create'),
    path('<int:article_pk>/', views.article_detail, name='article_detail'),
    path('<int:article_pk>/update/', views.article_update, name='article_update'),
    path('<int:article_pk>/delete/', views.article_delete, name='article_delete'),
    path('<int:article_pk>/comment-create/', views.comment_create, name='comment_create'),
    path('<int:article_pk>/comment-list/', views.comment_list, name='comment_list'),
    path('<int:article_pk>/comment-update/<int:comment_pk>/', views.comment_update, name='comment_update'),
    path('<int:article_pk>/comment-delete/<int:comment_pk>/', views.comment_delete, name='comment_delete'),
]
