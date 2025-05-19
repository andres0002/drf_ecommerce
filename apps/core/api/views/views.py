# py
# django
# drf
from rest_framework import viewsets
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
# third
# own

class GeneralListAPIView(ListAPIView):
    serializer_class = None
    serializer_view_class = None
    
    def get_queryset(self, pk=None):
        model = self.get_serializer().Meta.model
        return model.objects.filter(is_active=True)
    
    def get_serializer_class(self):
        if self.request.method == 'GET' and self.serializer_view_class is not None:
            return self.serializer_view_class
        return self.serializer_class

class GeneralListCreateAPIView(ListCreateAPIView):
    serializer_class = None
    serializer_view_class = None
    
    def get_queryset(self, pk=None):
        model = self.get_serializer().Meta.model
        return model.objects.filter(is_active=True)
    
    def get_serializer_class(self):
        if self.request.method == 'GET' and self.serializer_view_class is not None:
            return self.serializer_view_class
        return self.serializer_class

class GeneralRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = None
    serializer_view_class = None
    
    def get_queryset(self, pk=None):
        model = self.get_serializer().Meta.model
        if pk is None:
            return model.objects.filter(is_active=True)
        return model.objects.filter(is_active=True, pk=pk).first()
    
    def get_serializer_class(self):
        if self.request.method == 'GET' and self.serializer_view_class is not None:
            return self.serializer_view_class
        return self.serializer_class

class GeneralModelViewSets(viewsets.ModelViewSet):
    serializer_class = None
    serializer_view_class = None  # Solo para lectura.
    
    def get_serializer_class(self):
        # Si es un método de solo lectura (list o retrieve), usa el serializer de vista.
        if self.action in ['list', 'retrieve'] and self.serializer_view_class:
            return self.serializer_view_class
        return self.serializer_class  # Para otros métodos (create, update, etc.).

    def get_queryset(self):
        # Modificar el queryset para obtener solo objects activos.
        model = self.get_serializer().Meta.model
        return model.objects.filter(is_active=True)
    
    # elimination de todos los registers.
    @action(detail=False, methods=['delete'], url_path='bulk-delete')
    def bulk_delete(self, request):
        ids = request.data.get('ids', [])
        if not isinstance(ids, list):
            return Response({'error': 'ids must be a list'}, status=status.HTTP_400_BAD_REQUEST)
        # elimination direct.
        # deleted, _ = self.get_queryset().filter(id__in=ids).delete()
        # return Response({'deleted': deleted}, status=status.HTTP_204_NO_CONTENT)
        # elimination logical.
        updated_count = self.get_queryset().filter(id__in=ids).update(is_active=False)
        return Response({'deactivated': updated_count}, status=status.HTTP_204_NO_CONTENT)
        # { request.
        #     "ids": [1, 2, 3]
        # }