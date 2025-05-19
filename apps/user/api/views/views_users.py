# py
# django
# drf
from rest_framework.response import Response
from rest_framework import status
# third
# own
from apps.core.api.views.views import (
    GeneralModelViewSets
)
from apps.user.api.serializers.serializers import (
    UsersViewSerializer,
    UsersActionsSerializer
)

# Create your views here.

class UsersModelViewSets(GeneralModelViewSets):
    serializer_view_class = UsersViewSerializer
    serializer_class = UsersActionsSerializer
    
    # elimination logical -> si se quiere eliminar de forma directa solo comentar el method destroy().
    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        if user:
            user.is_active = False
            user.save()
            return Response({'message':'Successfully User elimination.'},status=status.HTTP_200_OK)
        return Response({'messge':'Errorful User elimination.'},status=status.HTTP_400_BAD_REQUEST)