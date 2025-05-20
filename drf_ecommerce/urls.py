"""
URL configuration for drf_ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# py
# django
from django.contrib import admin
from django.urls import path, include
# from django.contrib.auth.decorators import login_required
# drf
from rest_framework import permissions
# third
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# own

schema_view = get_schema_view(
    openapi.Info(
        title="Documentation API Ecommerce.",
        default_version='v0.1',
        description="Documentation API Ecommerce",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="frivandres038@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    # en el False debe ir la variable de .env.
    public=False if False else True,
    permission_classes=(permissions.IsAuthenticated if False else permissions.AllowAny,),
)

urlpatterns = [
    # swagger documentation.
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path('swagger<format>/', login_required(schema_view.without_ui(cache_timeout=0)), name='schema-json'),
    # path('swagger/', login_required(schema_view.with_ui('swagger', cache_timeout=0)), name='schema-swagger-ui'),
    # path('redoc/', login_required(schema_view.with_ui('redoc', cache_timeout=0)), name='schema-redoc'),
    # urls project drf_ecommerce.
    path('admin/', admin.site.urls),
    path('auth/', include(('apps.features.auth_own.api.urls.urls','auth'))),
    path('user/', include(('apps.features.user.api.urls.routers','user'))),
    path('product/', include(('apps.features.product.api.urls.routers','product'))),
]