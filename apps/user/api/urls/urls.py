# py
# django
from django.urls import path
# drf
# third
# own
from apps.user.api.views.views import UsersAPIView, UsersActionsByPkAPIView
from apps.user.api.views.views_functionts import users_api_view, users_actions_by_pk_api_view

urlpatterns = [
    # class.
    path('users/', UsersAPIView.as_view(), name='users'),
    path('users/<int:pk>/', UsersActionsByPkAPIView.as_view(), name='users_actions'),
    # functions.
    # path('users_funct/', users_api_view, name='users_funct'),
    # path('users_funct/<int:pk>/', users_actions_by_pk_api_view, name='users_funct_actions'),
]