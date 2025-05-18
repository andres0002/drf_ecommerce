# py
# django
from django.urls import path
# drf
# third
# own
from apps.user.api.views.views import (
    UsersListCreateAPIView,
    UsersRetrieveUpdateDestroyAPIView
)

# users.
urlpatterns = [
    path('users/', UsersListCreateAPIView.as_view(), name='users'),
    path('users/<int:pk>/', UsersRetrieveUpdateDestroyAPIView.as_view(), name='users_actions'),
]