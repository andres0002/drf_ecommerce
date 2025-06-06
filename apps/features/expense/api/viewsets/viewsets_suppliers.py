# py
# django
# drf
from rest_framework.response import Response
from rest_framework import status
# thrid
# own
from apps.core.api.viewsets.viewsets import (
    PublicGeneralViewSets,
    PrivateGeneralModelViewSets
)
from apps.features.expense.api.serializers.serializers import (
    SuppliersViewSerializer,
    SuppliersActionsSerializer
)

class PublicSuppliersViewSets(PublicGeneralViewSets):
    serializer_class = SuppliersActionsSerializer
    serializer_view_class = SuppliersViewSerializer
    
    def list(self, request, *args, **kwargs):
        suppliers = self.get_queryset()
        suppliers_serializer = self.get_serializer(suppliers, many = True)
        return Response(suppliers_serializer.data,status=status.HTTP_200_OK)

class PrivateSuppliersModelViewSets(PrivateGeneralModelViewSets):
    serializer_class = SuppliersActionsSerializer
    serializer_view_class = SuppliersViewSerializer

    # elimination logical. -> para elimination direct se comenta el method destroy().
    def destroy(self, request, *args, **kwargs):
        supplier = self.get_object()
        if supplier:
            supplier.is_active = False
            supplier.save()
            return Response({'message':'Successfully Supplier elimination.'},status=status.HTTP_200_OK)
        return Response({'messge':'Errorful Supplier elimination.'},status=status.HTTP_400_BAD_REQUEST)