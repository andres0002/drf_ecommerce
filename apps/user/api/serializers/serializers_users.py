# py
# django
# drf
from rest_framework import serializers
# third
# own
from apps.user.models import Users

class UsersSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(write_only=True, required=False) # write_only -> se ve solo en request -> qas o prd.
    # password = serializers.CharField(required=False) # se ve tanto en request como en response -> dev.
    last_login = serializers.DateTimeField(read_only=True)  # Solo lectura.
    created_at = serializers.DateTimeField(read_only=True)  # Solo lectura.
    updated_at = serializers.DateTimeField(read_only=True)  # Solo lectura.
    deleted_at = serializers.DateTimeField(read_only=True)  # Solo lectura.
    
    class Meta:
        model = Users
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Detecta si es creación (POST), no hay instance.
        if self.instance is None:
            self.fields['username'].required = True
            self.fields['email'].required = True
            self.fields['password'].required = True
    
    def create(self, validated_data):
        # obtine el password y lo elimina del context, para que no se guarde como text palno.
        password = validated_data.pop('password', None)
        user = Users(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        # obtine el password y lo elimina del context, para que no se guarde como text palno.
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance