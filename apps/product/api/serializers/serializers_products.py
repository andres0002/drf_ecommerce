# py
# django
# drf
from rest_framework import serializers
# third
# own
from apps.product.models import Products
from apps.product.api.serializers.serializers_measure_units import MeasureUnitsSerializer
from apps.product.api.serializers.serializers_categories_product import CategoriesProductSerializer

class ProductsViewSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(write_only=True, required=False)  # Solo en request for updation.
    created_at = serializers.DateTimeField(read_only=True)  # Solo lectura.
    updated_at = serializers.DateTimeField(read_only=True)  # Solo lectura.
    deleted_at = serializers.DateTimeField(read_only=True)  # Solo lectura.
    
    measure_unit = MeasureUnitsSerializer()
    category = CategoriesProductSerializer()
    
    class Meta:
        model = Products
        fields = '__all__'

class ProductsActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        exclude = ('id','is_active','created_at','updated_at','deleted_at')
    
    def to_representation(self, instance):
        return {
            "id": instance.id,
            "name": instance.name,
            "description": instance.description,
            "measure_unit": {
                'id': instance.measure_unit.id,
                'description': instance.measure_unit.description
            } if instance.measure_unit is not None else '',
            "category": {
                'id': instance.category.id,
                'description': instance.category.description
            } if instance.category is not None else '',
            "image": instance.image if (instance.image != '' and instance.image != None)  else ''
        }