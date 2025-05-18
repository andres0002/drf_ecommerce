# py
# django
# drf
from rest_framework import serializers
# third
# own
from apps.product.models import Products
from apps.product.api.serializers.serializers_generals import (
    MeasureUnitsSerializer,
    CategoriesProductSerializer
)

class ProductsViewSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(write_only=True, required=False)  # Solo en request for updation.
    created_at = serializers.DateTimeField(read_only=True)  # Solo lectura.
    updated_at = serializers.DateTimeField(read_only=True)  # Solo lectura.
    deleted_at = serializers.DateTimeField(read_only=True)  # Solo lectura.
    
    # method 1 -> FK -> me trae toda la data definida en el serializer del model en questión.
    measure_unit = MeasureUnitsSerializer()
    category = CategoriesProductSerializer()
    
    class Meta:
        model = Products
        fields = '__all__'

class ProductsActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        exclude = ('id','is_active','created_at','updated_at','deleted_at')

# method 1 -> FK -> me trae toda la data definida en el serializer del model en questión.
    # measure_unit = MeasureUnitsSerializer()
    # category = CategoriesProductSerializer()
    
    # method 2 -> FK -> se toma lo que se alla definido en el method __str__.
    # measure_unit = serializers.StringRelatedField()
    # category = serializers.StringRelatedField()
    
    # method 3 -> FK -> en el method to_representation(), para definir como quiero
    # que me muestre cada product.
    # def to_representation(self, instance):
    #     return {
    #         'id': instance.id,
    #         'name': instance.name,
    #         'description': instance.description,
    #         'measure_unit': {
    #             'id': instance.measure_unit.id,
    #             'description': instance.measure_unit.description
    #         },
    #         'category': {
    #             'id': instance.category.id,
    #             'description': instance.category.description
    #         },
    #         'image': instance.image if instance.image != '' else ''
    #     }