# py
# django
# drf
from rest_framework.response import Response
from rest_framework import status
# thrid
# own
from apps.core.api.views.views import (
    GeneralModelViewSets
)
from apps.features.product.api.serializers.serializers import  (
    MeasureUnitsViewSerializer,
    MeasureUnitsActionsSerializer
)

class MeasureUnitsModelViewSets(GeneralModelViewSets):
    serializer_view_class = MeasureUnitsViewSerializer
    serializer_class = MeasureUnitsActionsSerializer

    # elimination logical. -> para elimination direct se comenta el method destroy().
    def destroy(self, request, *args, **kwargs):
        measure_unit = self.get_object()
        if measure_unit:
            measure_unit.is_active = False
            measure_unit.save()
            return Response({'message':'Successfully Measure Unit elimination.'},status=status.HTTP_200_OK)
        return Response({'messge':'Errorful Measure Unit elimination.'},status=status.HTTP_400_BAD_REQUEST)