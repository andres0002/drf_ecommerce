# py
# django
# drf
from rest_framework.response import Response
from rest_framework import status
# thrid
# own
from apps.core.api.views.views import (
    GeneralListCreateAPIView,
    GeneralRetrieveUpdateDestroyAPIView
)
from apps.product.api.serializers.serializers import IndicatorsActionsSerializer

class IndicatorsListCreateAPIView(GeneralListCreateAPIView):
    serializer_class = IndicatorsActionsSerializer

class IndicatorsRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = IndicatorsActionsSerializer

    # elimination logical. -> para elimination direct se comenta el method delete().
    def delete(self, request, pk, *args, **kwargs):
        indicator = self.get_queryset(pk)
        if indicator:
            indicator.is_active = False
            indicator.save()
            return Response({'message':'Successfully Category Product elimination.'},status=status.HTTP_200_OK)
        return Response({'messge':'Errorful Category Product elimination.'},status=status.HTTP_400_BAD_REQUEST)