# py
# django
# drf
from rest_framework import serializers
# third
# own
from apps.product.models import MeasureUnits

class MeasureUnitsSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(write_only=True)  # Solo en request for updation.
    created_at = serializers.DateTimeField(read_only=True)  # Solo lectura.
    updated_at = serializers.DateTimeField(read_only=True)  # Solo lectura.
    deleted_at = serializers.DateTimeField(read_only=True)  # Solo lectura.
    
    class Meta:
        model = MeasureUnits
        fields = '__all__'