# py
# django
# drf
from rest_framework import serializers
# third
# own
from apps.product.models import Products
from apps.product.api.serializers.serializers_measure_units import MeasureUnitsViewSerializer
from apps.product.api.serializers.serializers_categories_product import CategoriesProductViewSerializer

class ProductsViewSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Products
        fields = '__all__'
    
    measure_unit = MeasureUnitsViewSerializer()
    category = CategoriesProductViewSerializer()

class ProductsActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        exclude = ('id','is_active','created_at','updated_at','deleted_at')