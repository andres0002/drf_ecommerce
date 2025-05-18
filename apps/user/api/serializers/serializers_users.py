# py
# django
from django.contrib.auth.models import Group, Permission
# drf
from rest_framework import serializers
# third
# own
from apps.user.models import Users

class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class UserPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'codename', 'name']

class UsersViewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(write_only=True, required=False) # write_only -> se ve solo en request -> qas o prd.
    # password = serializers.CharField(required=False) # se ve tanto en request como en response -> dev.
    last_login = serializers.DateTimeField(read_only=True)  # Solo lectura.
    created_at = serializers.DateTimeField(read_only=True)  # Solo lectura.
    updated_at = serializers.DateTimeField(read_only=True)  # Solo lectura.
    deleted_at = serializers.DateTimeField(read_only=True)  # Solo lectura.
    # READ: Mostrar grupos y permisos anidados
    groups = GroupsSerializer(many=True, read_only=True)
    user_permissions = UserPermissionsSerializer(many=True, read_only=True)
    
    class Meta:
        model = Users
        fields = '__all__'

class UsersActionsSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(write_only=True, required=False) # write_only -> se ve solo en request -> qas o prd.
    # password = serializers.CharField(required=False) # se ve tanto en request como en response -> dev.
    # READ: Mostrar grupos y permisos anidados
    groups = GroupsSerializer(many=True, read_only=True)
    user_permissions = UserPermissionsSerializer(many=True, read_only=True)
    # WRITE: Enviar solo los IDs
    group_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Group.objects.all(),
        write_only=True,
        source='groups',
        required=False
    )
    permission_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Permission.objects.all(),
        write_only=True,
        source='user_permissions',
        required=False
    )
    
    class Meta:
        model = Users
        exclude = ('id','is_active','is_staff','is_superuser','last_login','created_at','updated_at','deleted_at')
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.username,
            'email': instance.email,
            'name': instance.name,
            'lastname': instance.lastname,
            'groups': GroupsSerializer(instance.groups.all(), many=True).data,
            'user_permissions': UserPermissionsSerializer(instance.user_permissions.all(), many=True).data,
            'image': instance.image if (instance.image != '' and instance.image != None)  else ''
        }
    
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
        groups = validated_data.pop('groups', [])
        permissions = validated_data.pop('user_permissions', [])
        user = Users(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        if groups:
            user.groups.set(groups)
        if permissions:
            user.user_permissions.set(permissions)
        return user

    def update(self, instance, validated_data):
        # obtine el password y lo elimina del context, para que no se guarde como text palno.
        password = validated_data.pop('password', None)
        groups = validated_data.pop('groups', None)
        permissions = validated_data.pop('user_permissions', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        if groups is not None:
            instance.groups.set(groups)
        if permissions is not None:
            instance.user_permissions.set(permissions)
        return instance