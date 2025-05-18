# py
# django
from django.urls import path
# from django.urls import path
# drf
# third
# own
from apps.product.api.views.views import (
    CategoriesProductListCreateAPIView,
    CategoriesProductRetrieveUpdateDestroyAPIView
)

# categories product.
urlpatterns = [
    path('categories_product/', CategoriesProductListCreateAPIView.as_view(), name='categories_product'),
    path('categories_product/<int:pk>/', CategoriesProductRetrieveUpdateDestroyAPIView.as_view(), name='categories_product_actions'),
    
]