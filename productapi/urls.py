from django.urls import path
from productapi.views import  BrandList, BrandDetail, ProductList, ProductDetail

urlpatterns = [
    path('brands/', BrandList.as_view()),
    path('brands/<int:pk>', BrandDetail.as_view()),

    path('products/', ProductList.as_view()),
    path('products/<int:pk>', ProductDetail.as_view()),
]