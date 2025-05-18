# py
# django
from django.urls import path
# from django.urls import path
# drf
# third
# own
from apps.product.api.views.views import (
    MeasureUnitsListAPIView,
    CategoriesProductListAPIView,
    IndicatorsListAPIView,
    ProductsListAPIView,
    ProductsCreateAPIView,
    ProductsRetrieveAPIView,
    ProductsDestroyAPIView,
    ProductsUpdateAPIView
)

urlpatterns = [
    path('measure_units/', MeasureUnitsListAPIView.as_view(), name='measure_units'),
    path('categories_product/', CategoriesProductListAPIView.as_view(), name='categories_product'),
    path('indicators/', IndicatorsListAPIView.as_view(), name='indicators'),
    path('products/', ProductsListAPIView.as_view(), name='products'),
    path('products/create/', ProductsCreateAPIView.as_view(), name='products_create'),
    path('products/detail/<int:pk>/', ProductsRetrieveAPIView.as_view(), name='products_detail'),
    path('products/delete/<int:pk>/', ProductsDestroyAPIView.as_view(), name='products_delete'),
    path('products/update/<int:pk>/', ProductsUpdateAPIView.as_view(), name='products_update'),
]