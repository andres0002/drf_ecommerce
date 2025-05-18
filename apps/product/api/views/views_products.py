# py
# django
# drf
from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
# third
# own
from apps.core.api.views.views import (
    GeneralListAPIView
)
from apps.product.api.serializers.serializers import (
    ProductsViewSerializer,
    ProductsActionsSerializer
)

class ProductsListAPIView(GeneralListAPIView):
    serializer_class = ProductsViewSerializer

class ProductsCreateAPIView(CreateAPIView):
    serializer_class = ProductsActionsSerializer

    def post(self, request, *args, **kwargs):
        product_serializer = self.serializer_class(data=request.data)
        # validation.
        if product_serializer.is_valid():
            product_serializer.save()
            return Response({'message':'Successfully Product register.'},status=status.HTTP_201_CREATED)
        return Response(product_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductsRetrieveAPIView(RetrieveAPIView):
    serializer_class = ProductsViewSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(is_active=True)

# elimination direct -> sin el method delete.
class ProductsDestroyAPIView(DestroyAPIView):
    serializer_class = ProductsActionsSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(is_active=True)

    # elimination logical.
    def delete(self, request, pk, *args, **kwargs):
        product = self.get_queryset().filter(pk=pk).first()
        if product:
            product.is_active = False
            product.save()
            return Response({'message':'Successfully Product elimination.'},status=status.HTTP_200_OK)
        return Response({'messge':'Errorful Product elimination.'},status=status.HTTP_400_BAD_REQUEST)

class ProductsUpdateAPIView(UpdateAPIView):
    serializer_class = ProductsActionsSerializer
    
    def get_queryset(self, pk):
        return self.get_serializer().Meta.model.objects.filter(is_active=True).filter(pk=pk).first()
    
    def patch(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(product_serializer.data,status=status.HTTP_200_OK)
        return Response({'messge':'Product no exist.'},status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data,status=status.HTTP_200_OK)
            return Response(product_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response({'messge':'Product no exist.'},status=status.HTTP_400_BAD_REQUEST)