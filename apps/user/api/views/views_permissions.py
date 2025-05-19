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
    UserPermissionsViewSerializer,
    UserPermissionsActionsSerializer
)

# Create your views here.

class UserPermissionsModelViewSets(GeneralModelViewSets):
    serializer_view_class = UserPermissionsViewSerializer
    serializer_class = UserPermissionsActionsSerializer
    
    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.all()