# py
# django
# drf
from rest_framework.generics import ListAPIView
# third
# own

class GeneralListAPIView(ListAPIView):
    serializer_class = None
    
    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(is_active=True)