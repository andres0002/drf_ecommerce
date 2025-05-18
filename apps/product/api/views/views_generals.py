# py
# django
# drf
# thrid
# own
from apps.core.api.views.views import (
    GeneralListAPIView
)
from apps.product.api.serializers.serializers import (
    MeasureUnitsSerializer,
    CategoriesProductSerializer,
    IndicatorsSerializer
)

class MeasureUnitsListAPIView(GeneralListAPIView):
    serializer_class = MeasureUnitsSerializer

class CategoriesProductListAPIView(GeneralListAPIView):
    serializer_class = CategoriesProductSerializer

class IndicatorsListAPIView(GeneralListAPIView):
    serializer_class = IndicatorsSerializer