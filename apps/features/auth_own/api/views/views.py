# py
from datetime import datetime
# django
from django.contrib.auth import logout
from django.contrib.sessions.models import Session
# drf
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
# third
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# own
from apps.features.user.models import Users
from apps.features.user.api.serializers.serializers import UsersViewSerializer

# Create your views here.

class Login(ObtainAuthToken):
    
    @swagger_auto_schema(
        tags=["🔹 Auth"],
        operation_id="auth",
        operation_description="Login de usuario y generación de token.",
        responses={
            200: openapi.Response(description="Inicio de sesión exitoso"),
            400: "Credenciales inválidas",
            401: "Usuario inactivo",
            409: "Usuario ya autenticado"
        }
    )
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context={'request':request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = UsersViewSerializer(user)
                if created:
                    return Response({
                        "token": token.key,
                        "user": user_serializer.data,
                        "message": "Inicio de sesión exitoso."
                    }, status=status.HTTP_200_OK)
                else:
                    # Eliminar el token del usuario
                    token.delete()
                    return Response({
                        'error': 'Ya se ha iniciado sesión con este user.'
                    },  status=status.HTTP_409_CONFLICT)
            else:
                return Response({'error':'Este usuario no puede iniciar sesión.'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'error':'Username o Password incorrectos'}, status=status.HTTP_400_BAD_REQUEST)

class Logout(APIView):
    permission_classes = (IsAuthenticated,)
    
    @swagger_auto_schema(
        tags=["🔹 Auth"],
        operation_id="auth_logout",
        operation_description="Logout de usuario, elimina token y sesiones activas.",
        responses={
            200: openapi.Response(description="Logout exitoso"),
            401: "Credenciales inválidas o no autenticado"
        }
    )
    def post(self, request, *args, **kwargs):
        user = request.user
        
        token = Token.objects.filter(user=user).first()
        
        # Eliminar sesiones activas del usuario
        sessions = Session.objects.filter(expire_date__gte=datetime.now())
        deleted_sessions = 0

        for session in sessions:
            data = session.get_decoded()
            if str(user.id) == str(data.get('_auth_user_id')):
                session.delete()
                deleted_sessions += 1
        
        # Eliminar el token del usuario
        token.delete()
        
        return Response({
            "token_message": "Token eliminado correctamente.",
            "session_message": f"{deleted_sessions} sesión(es) eliminada(s)."
        }, status=status.HTTP_200_OK)

class UserTokenRefresh(APIView):
    # permission_classes = (IsAuthenticated,)
    
    @swagger_auto_schema(
        tags=["🔹 Auth"],
        operation_id="actualizar_token",
        operation_description="Actualización de token.",
        manual_parameters=[
            openapi.Parameter(
                'username',
                openapi.IN_QUERY,
                description="Username de la sesión.",
                type=openapi.TYPE_STRING,
                required=True
            )
        ],
        responses={
            200: openapi.Response(description="Actualización del token exitoso"),
            400: "Username no proporcionado",
            404: "Usuario no encontrado"
        }
    )
    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')

        if not username:
            return Response({"error": "Username no proporcionado."}, status=status.HTTP_400_BAD_REQUEST)

        user = Users.objects.filter(username=username).first()
        if not user:
            return Response({"error": "Usuario no encontrado."}, status=status.HTTP_404_NOT_FOUND)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_200_OK)