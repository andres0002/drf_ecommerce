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
from apps.user.api.serializers.serializers import UsersActionsSerializer

# Create your views here.

class UsersListCreateAPIView(GeneralListCreateAPIView):
    serializer_class = UsersActionsSerializer

class UsersRetrieveUpdateDestroyAPIView(GeneralRetrieveUpdateDestroyAPIView):
    serializer_class = UsersActionsSerializer
    
    # elimination logical -> si se quiere eliminar de forma directa solo comentar el method delete().
    def delete(self, request, pk, *args, **kwargs):
        user = self.get_queryset(pk)
        if user:
            user.is_active = False
            user.save()
            return Response({'message':'Successfully User elimination.'},status=status.HTTP_200_OK)
        return Response({'messge':'Errorful User elimination.'},status=status.HTTP_400_BAD_REQUEST)