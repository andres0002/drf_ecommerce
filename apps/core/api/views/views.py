# py
# django
# drf
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
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