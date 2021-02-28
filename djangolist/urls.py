from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url 
from .views import ProductListView, ProductListInfiniteView

urlpatterns = [
    path('', ProductListInfiniteView.as_view(), name='home'),
    path('listing/', ProductListView.as_view(),name="productlist"),
    
]