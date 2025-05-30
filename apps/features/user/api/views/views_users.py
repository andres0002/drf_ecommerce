# py
# django
# drf
from rest_framework.response import Response
from rest_framework import status
# third
# own
from apps.core.api.views.views import (
    PublicGeneralViewSets,
    PrivateGeneralModelViewSets
)
from apps.features.user.api.serializers.serializers import (
    UsersViewSerializer,
    UsersActionsSerializer
)

# Create your views here.

class PublicUsersViewSets(PublicGeneralViewSets):
    serializer_class = UsersActionsSerializer
    serializer_view_class = UsersViewSerializer
    
    def list(self, request, *args, **kwargs):
        users = self.get_queryset()
        users_serializer = self.get_serializer(users, many = True)
        return Response(users_serializer.data,status=status.HTTP_200_OK)

class PrivateUsersModelViewSets(PrivateGeneralModelViewSets):
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