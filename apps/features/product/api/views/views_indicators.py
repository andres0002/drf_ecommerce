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
from apps.features.product.api.serializers.serializers import (
    IndicatorsViewSerializer,
    IndicatorsActionsSerializer
)

class IndicatorsModelViewSets(GeneralModelViewSets):
    serializer_view_class = IndicatorsViewSerializer
    serializer_class = IndicatorsActionsSerializer

    # elimination logical. -> para elimination direct se comenta el method delete().
    def destroy(self, request, *args, **kwargs):
        indicator = self.get_object()
        if indicator:
            indicator.is_active = False
            indicator.save()
            return Response({'message':'Successfully Category Product elimination.'},status=status.HTTP_200_OK)
        return Response({'messge':'Errorful Category Product elimination.'},status=status.HTTP_400_BAD_REQUEST)