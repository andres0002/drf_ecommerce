# py
# django
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# third
from simple_history.models import HistoricalRecords
# own

# Create your models here.

class UsersManager(BaseUserManager):
    def _create_user(self, username, email, name, lastname, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            name = name,
            lastname = lastname,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        if password not in [None, '']:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, name, lastname, password=None, is_staff=False, is_superuser=False, **extra_fields):
        return self._create_user(username, email, name, lastname, password, is_staff, is_superuser, **extra_fields)

    def create_superuser(self, username, email, name, lastname, password=None, is_staff=True, is_superuser=True, **extra_fields):
        return self._create_user(username, email, name, lastname, password, is_staff, is_superuser, **extra_fields)

    def get_by_natural_key(self, username):
        return self.get(username=username)

class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='user/profile/image/', max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    historical = HistoricalRecords()
    objects = UsersManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'lastname']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['username']
    
    def natural_key(self):
        return (self.username,)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if self.pk:
            # Si es una actualización, verificamos si cambió la contraseña
            old = Users.objects.filter(pk=self.pk).first()
            if old and old.password != self.password:
                if not self.password.startswith('pbkdf2_sha256$'):
                    self.set_password(self.password)
        else:
            # Usuario nuevo, se asegura que la contraseña esté hasheada
            if self.password and not self.password.startswith('pbkdf2_sha256$'):
                self.set_password(self.password)
        super().save(*args, **kwargs)