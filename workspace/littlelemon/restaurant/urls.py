#define URL route for index() view
from django.urls import path, include
from . import views
from rest_framework import viewsets


urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    
]
