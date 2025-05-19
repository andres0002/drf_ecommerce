# py
# django
# from django.urls import path
# drf
from rest_framework.routers import DefaultRouter
# third
# own
from apps.product.api.views.views import (
    MeasureUnitsModelViewSets,
    CategoriesProductModelViewSets,
    IndicatorsModelViewSets,
    ProductsModelViewSets
)

router = DefaultRouter()

# measure units.
router.register(r'measure_units', MeasureUnitsModelViewSets, basename='measure_units')
# categories product.
router.register(r'categories_product', CategoriesProductModelViewSets, basename='categories_product')
# indicators.
router.register(r'indicators', IndicatorsModelViewSets, basename='indicators')
# products.
router.register(r'products', ProductsModelViewSets, basename='products')

# instance urlpatterns.
urlpatterns = []
# populate instance.
urlpatterns += router.urls

# print('URLPATTERNS:', urlpatterns)
# for url in urlpatterns:
#     print(url)