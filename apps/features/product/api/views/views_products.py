# py
# django
# drf
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# third
# own
from apps.core.api.views.views import (
    GeneralModelViewSets
)
from apps.features.product.api.serializers.serializers import (
    ProductsViewSerializer,
    ProductsActionsSerializer
)

class ProductsModelViewSets(GeneralModelViewSets):
    """
        Comments main.
    """
    # permission_classes = (IsAuthenticated,)
    serializer_view_class = ProductsViewSerializer
    serializer_class = ProductsActionsSerializer
    
    def create(self, request, *args, **kwargs):
        """
            Comments endpoints.
            
            
            dfsdfds
        """
        product_serializer = self.serializer_class(data=request.data)
        # validation.
        if product_serializer.is_valid():
            product_serializer.save()
            return Response({'message':'Successfully Product register.'},status=status.HTTP_201_CREATED)
        return Response(product_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, *args, **kwargs):
        if self.get_object():
            product_serializer = self.serializer_class(self.get_object())
            return Response(product_serializer.data,status=status.HTTP_200_OK)
        return Response({'messge':'Product no exist.'},status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        if self.get_object():
            product_serializer = self.serializer_class(self.get_object(), data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data,status=status.HTTP_200_OK)
            return Response(product_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response({'messge':'Product no exist.'},status=status.HTTP_400_BAD_REQUEST)
    
    # elimination logical. -> para elimination direct se comenta el method delete().
    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        if product:
            product.is_active = False
            product.save()
            return Response({'message':'Successfully Product elimination.'},status=status.HTTP_200_OK)
        return Response({'messge':'Errorful Product elimination.'},status=status.HTTP_400_BAD_REQUEST)