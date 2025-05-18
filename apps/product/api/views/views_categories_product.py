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
from apps.product.api.serializers.serializers import CategoriesProductSerializer

class CategoriesProductListCreateAPIView(GeneralListCreateAPIView):
    serializer_class = CategoriesProductSerializer

class CategoriesProductRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = CategoriesProductSerializer
    
    # elimination logical. -> para elimination direct se comenta el method delete().
    def delete(self, request, pk, *args, **kwargs):
        category_product = self.get_queryset(pk)
        if category_product:
            category_product.is_active = False
            category_product.save()
            return Response({'message':'Successfully Category Product elimination.'},status=status.HTTP_200_OK)
        return Response({'messge':'Errorful Category Product elimination.'},status=status.HTTP_400_BAD_REQUEST)