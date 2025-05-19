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
from apps.product.api.serializers.serializers import (
    CategoriesProductViewSerializer,
    CategoriesProductActionsSerializer
)

class CategoriesProductModelViewSets(GeneralModelViewSets):
    serializer_view_class = CategoriesProductViewSerializer
    serializer_class = CategoriesProductActionsSerializer

    # elimination logical. -> para elimination direct se comenta el method destroy().
    def destroy(self, request, *args, **kwargs):
        category_product = self.get_object()
        if category_product:
            category_product.is_active = False
            category_product.save()
            return Response({'message':'Successfully Category Product elimination.'},status=status.HTTP_200_OK)
        return Response({'messge':'Errorful Category Product elimination.'},status=status.HTTP_400_BAD_REQUEST)