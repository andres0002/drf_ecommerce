# py
# django
# drf
from rest_framework.response import Response
from rest_framework import status
# third
# own
from apps.core.api.views.views import (
    GeneralListCreateAPIView,
    GeneralRetrieveUpdateDestroyAPIView
)
from apps.product.api.serializers.serializers import (
    ProductsActionsSerializer
)

class ProductsListCreateAPIView(GeneralListCreateAPIView):
    serializer_class = ProductsActionsSerializer

    def post(self, request, *args, **kwargs):
        product_serializer = self.serializer_class(data=request.data)
        # validation.
        if product_serializer.is_valid():
            product_serializer.save()
            return Response({'message':'Successfully Product register.'},status=status.HTTP_201_CREATED)
        return Response(product_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductsRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = ProductsActionsSerializer
    
    def patch(self, request, pk=None, *args, **kwargs):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(product_serializer.data,status=status.HTTP_200_OK)
        return Response({'messge':'Product no exist.'},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None, *args, **kwargs):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data,status=status.HTTP_200_OK)
            return Response(product_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response({'messge':'Product no exist.'},status=status.HTTP_400_BAD_REQUEST)
    
    # elimination logical. -> para elimination direct se comenta el method delete().
    def delete(self, request, pk, *args, **kwargs):
        product = self.get_queryset(pk)
        if product:
            product.is_active = False
            product.save()
            return Response({'message':'Successfully Product elimination.'},status=status.HTTP_200_OK)
        return Response({'messge':'Errorful Product elimination.'},status=status.HTTP_400_BAD_REQUEST)