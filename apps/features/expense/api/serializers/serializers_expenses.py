# py
# django
# drf
from rest_framework import serializers
# third
# own
from apps.features.expense.models import Expenses

class ExpensesViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = '__all__'

class ExpensesActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        exclude = ('id','is_active','created_at','updated_at','deleted_at')