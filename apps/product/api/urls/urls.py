# py
# django
# from django.urls import path
# drf
# third
# own
from apps.product.api.urls.urls_categories_product import urlpatterns as urls_categories_product
from apps.product.api.urls.urls_measure_units import urlpatterns as urls_measure_units
from apps.product.api.urls.urls_indicators import urlpatterns as urls_indicators
from apps.product.api.urls.urls_products import urlpatterns as urls_products

# instance de urlpatterns.
urlpatterns = []
# measure units.
urlpatterns += urls_measure_units
# categories product.
urlpatterns += urls_categories_product
# indicators.
urlpatterns += urls_indicators
# products.
urlpatterns += urls_products