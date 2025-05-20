# py
# django
# drf
from rest_framework.routers import DefaultRouter
# third
# own
from apps.features.user.api.views.views import (
    GroupsModelViewSets,
    UserPermissionsModelViewSets,
    UsersModelViewSets
)

router = DefaultRouter()

# users.
router.register(r'groups', GroupsModelViewSets, basename='groups')
router.register(r'user_permissions', UserPermissionsModelViewSets, basename='user_permissions')
router.register(r'users', UsersModelViewSets, basename='users')

# instance urlpatterns.
urlpatterns = []
# populate instance.
urlpatterns += router.urls

# print('URLPATTERNS:', urlpatterns)
# for url in urlpatterns:
#     print(url)