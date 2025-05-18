# py
# django
from django.urls import path
# drf
# third
# own
from apps.product.api.views.views import (
    ProductsListCreateAPIView,
    ProductsRetrieveUpdateDestroyAPIView
)

# products.
urlpatterns = [
    path('products/', ProductsListCreateAPIView.as_view(), name='products'),
    path('products/<int:pk>/', ProductsRetrieveUpdateDestroyAPIView.as_view(), name='products_actions'),
]