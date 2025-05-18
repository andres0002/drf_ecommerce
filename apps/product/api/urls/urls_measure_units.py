# py
# django
from django.urls import path
# from django.urls import path
# drf
# third
# own
from apps.product.api.views.views import (
    MeasureUnitsListCreateAPIView,
    MeasureUnitsRetrieveUpdateDestroyAPIView
)

# measure units.
urlpatterns = [
    path('measure_units/', MeasureUnitsListCreateAPIView.as_view(), name='measure_units'),
    path('measure_units/<int:pk>/', MeasureUnitsRetrieveUpdateDestroyAPIView.as_view(), name='measure_units_actions'),
    
]