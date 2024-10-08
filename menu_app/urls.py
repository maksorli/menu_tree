 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('punkt1/', views.punkt1_view, name='punkt1'),
    path('punkt2/', views.punkt2_view, name='punkt2'),
    path('<slug:slug>/', views.menu_item_view, name='menu_item'),
]
