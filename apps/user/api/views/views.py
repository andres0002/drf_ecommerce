# py
# django
from django.shortcuts import get_object_or_404
# drf
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# third
# own
from apps.core.utils.utils import validar_pk_numerico
from apps.user.models import Users
from apps.user.api.serializers.serializers import UsersSerializer

# Create your views here.

class UsersAPIView(APIView):
    model = Users
    serializer = UsersSerializer
    # list.
    def get(self, request, *args, **kwargs):
        # query.
        users = self.model.objects.filter(is_active=True)
        users_serializer = self.serializer(users, many = True)
        return Response(users_serializer.data,status=status.HTTP_200_OK)
    # create.
    def post(self, request, *args, **kwargs):
        user_serializer = self.serializer(data=request.data)
        # validation.
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data,status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UsersActionsByPkAPIView(APIView):
    model = Users
    serializer = UsersSerializer
    # retrieve.
    def get(self, request, pk, *args, **kwargs):
        # validation.
        pk, error_response = validar_pk_numerico(pk)
        if error_response:
            return error_response
        # query.
        # user = self.model.objects.filter(pk=pk).first()
        user = get_object_or_404(self.model, is_active=True, pk=pk)
        user_serializer = self.serializer(user)
        return Response(user_serializer.data,status=status.HTTP_200_OK)
    # update.
    def put(self, request, pk, *args, **kwargs):
        # validation.
        pk, error_response = validar_pk_numerico(pk)
        if error_response:
            return error_response
        # query.
        user = get_object_or_404(self.model, is_active=True, pk=pk)
        user_serializer = self.serializer(user, data=request.data)
        # validation.
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data,status=status.HTTP_200_OK)
        return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    # delete
    def delete(self, request, pk, *args, **kwargs):
        # validation.
        pk, error_response = validar_pk_numerico(pk)
        if error_response:
            return error_response
        # query.
        user = get_object_or_404(self.model, is_active=True, pk=pk)
        # elimination logical.
        user.is_active = False
        user.save()
        user_serializer = self.serializer(user)
        return Response(user_serializer.data,status.HTTP_200_OK)
        # elimination direct.
        # user.delete()
        # return Response({'message':'Successfully User elimination.'},status=status.HTTP_204_NO_CONTENT)