# py
# django
from django.urls import path
# drf
# third
# own
from apps.features.auth_own.api.views.views import Login, Logout, RefreshToken

urlpatterns = [
    # authtoken
    # path('login/', Login.as_view(), name='login'),
    # path('logout/', Logout.as_view(), name='logout'),
    # path('refresh_token/', RefreshToken.as_view(), name='refresh_token'),
    # simplejwt
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('refresh_token/', RefreshToken.as_view(), name='refresh_token'),
]