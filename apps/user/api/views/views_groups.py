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
    GroupsViewSerializer,
    GroupsActionsSerializer
)

# Create your views here.

class GroupsModelViewSets(GeneralModelViewSets):
    serializer_view_class = GroupsViewSerializer
    serializer_class = GroupsActionsSerializer
    
    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.all()