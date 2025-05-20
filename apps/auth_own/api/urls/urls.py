# py
# django
from django.urls import path
# drf
# third
# own
from apps.auth_own.api.views.views import Login, Logout, UserTokenRefresh

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('user_token_refresh/', UserTokenRefresh.as_view(), name='user_token_refresh'),
]