# py
# django
from django.urls import path
# from django.urls import path
# drf
# third
# own
from apps.product.api.views.views import (
    IndicatorsListCreateAPIView,
    IndicatorsRetrieveUpdateDestroyAPIView
)

# indicators.
urlpatterns = [
    path('indicators/', IndicatorsListCreateAPIView.as_view(), name='indicators'),
    path('indicators/<int:pk>/', IndicatorsRetrieveUpdateDestroyAPIView.as_view(), name='indicators_actions'),
    
]