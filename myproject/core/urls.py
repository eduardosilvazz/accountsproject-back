from django.urls import path, include
from .views import ProductList, ProductDetail, CategoryList, home
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', ),  
    path('products/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
]
