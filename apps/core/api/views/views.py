# py
# django
# drf
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
# third
from drf_yasg.inspectors import SwaggerAutoSchema
from drf_yasg.utils import swagger_auto_schema
# own
from apps.core.api.serializers.serializers import BulkDeleteSerializer

# Generar tag automatico de swagger por model.
class AutoTagSchema(SwaggerAutoSchema):
    def get_tags(self, operation_keys=None):
        serializer = self.view.get_serializer_class()
        model = getattr(serializer.Meta, 'model', None)
        if model:
            return [f"🔹 {model.__name__}"]
        return ['NoTag']

class GeneralModelViewSets(viewsets.ModelViewSet):
    serializer_class = None
    serializer_view_class = None  # Solo para lectura.
    swagger_schema = AutoTagSchema # para definir tag por model automaticamente.
    
    def get_serializer_class(self):
        # Si es un método de solo lectura (list o retrieve), usa el serializer de vista.
        if self.action in ['list', 'retrieve'] and self.serializer_view_class:
            return self.serializer_view_class
        return self.serializer_class  # Para otros métodos (create, update, etc.).

    def get_queryset(self):
        # Modificar el queryset para obtener solo objects activos.
        model = self.get_serializer().Meta.model
        return model.objects.filter(is_active=True)
    
    @swagger_auto_schema(
        method='delete',
        request_body=BulkDeleteSerializer,
        responses={204: 'No Content', 400: 'Bad Request'},
        operation_description="Desactiva múltiples objetos (borrado lógico)."
    )
    # elimination de todos los registers, logical.
    @action(detail=False, methods=['delete'], url_path='bulk_delete_logical')
    def bulk_delete_logical(self, request):
        ids = request.data.get('ids', [])
        if not isinstance(ids, list):
            return Response({'error': 'ids must be a list'}, status=status.HTTP_400_BAD_REQUEST)
        # elimination logical.
        updated_count = self.get_queryset().filter(id__in=ids).update(is_active=False)
        return Response({'deactivated': updated_count}, status=status.HTTP_204_NO_CONTENT)
    
    @swagger_auto_schema(
        method='delete',
        request_body=BulkDeleteSerializer,
        responses={204: 'No Content', 400: 'Bad Request'},
        operation_description="Elimina múltiples objetos de la DB (borrado directo)."
    )
    # elimination de todos los registers, direct.
    @action(detail=False, methods=['delete'], url_path='bulk_delete_direct')
    def bulk_delete_direct(self, request):
        ids = request.data.get('ids', [])
        if not isinstance(ids, list):
            return Response({'error': 'ids must be a list'}, status=status.HTTP_400_BAD_REQUEST)
        # elimination direct.
        deleted, _ = self.get_queryset().filter(id__in=ids).delete()
        return Response({'deleted': deleted}, status=status.HTTP_204_NO_CONTENT)