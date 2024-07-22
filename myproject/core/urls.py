from django.urls import path
from .views import ProductList, ProductDetail, CategoryList, home

urlpatterns = [
    path('', home, name='home'),  # This is the homepage URL
    path('products/', ProductList.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('categories/', CategoryList.as_view(), name='category_list'),
]
