# py
# django
# drf
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
# third
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
# own
from apps.core.api.views.views import (
    PublicGeneralViewSets,
    PrivateGeneralModelViewSets
)
from apps.features.user.api.serializers.serializers import (
    UsersViewSerializer,
    UsersActionsSerializer,
    UsersSetPasswordSerializer
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
    
    @swagger_auto_schema(
        request_body=UsersSetPasswordSerializer,
        responses={
            200: openapi.Response(description='Password actualizada correctamente.'),
            400: openapi.Response(description='Error de validación en la información enviada.')
        },
        # operation_summary="Actualizar contraseña del usuario", # comment endpoint.
        operation_description="Permite actualizar la contraseña del usuario autenticado usando su ID."
    )
    # detail in False -> para poner el enpoint direct "/user/private_users/set_password/"
    # detail in True -> para poner el enpoint despues del detail "/user/private_users/{id}/set_password/"
    @action(detail=True, methods=['post'])
    def set_password(self, request, *args, **kwargs):
        user = self.get_object()
        passwords_serializer = UsersSetPasswordSerializer(data=request.data)
        if passwords_serializer.is_valid():
            user.set_password(passwords_serializer.validated_data.get('password'))
            user.save()
            return Response({
                'message': 'Password de user actualizada successfully.'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'Hay errores en la info enviada.',
            'errors': passwords_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)