# py
# django
# drf
from rest_framework import serializers
# third
# own
from apps.product.models import Indicators
from apps.product.api.serializers.serializers_categories_product import CategoriesProductSerializer

class IndicatorsViewSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(write_only=True)  # Solo en request for updation.
    created_at = serializers.DateTimeField(read_only=True)  # Solo lectura.
    updated_at = serializers.DateTimeField(read_only=True)  # Solo lectura.
    deleted_at = serializers.DateTimeField(read_only=True)  # Solo lectura.
    
    category = CategoriesProductSerializer()
    
    class Meta:
        model = Indicators
        fields = '__all__'

class IndicatorsActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicators
        exclude = ('id','is_active','created_at','updated_at','deleted_at')
        
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'descount_value': instance.descount_value,
            'category': {
                'id': instance.category.id,
                'description': instance.description
            },
        }