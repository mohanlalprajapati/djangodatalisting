from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url 
from .views import ProductListView, ProductListInfiniteView
app_name = 'djangolist'
urlpatterns = [
    path('', ProductListInfiniteView.as_view(), name='infinitescroll'),
    path('listing/', ProductListView.as_view(),name="productlist"),
    
]