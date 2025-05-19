# py
# django
# drf
from rest_framework.routers import DefaultRouter
# third
# own
from apps.user.api.views.views import (
    UsersModelViewSets
)

router = DefaultRouter()

# users.
router.register(r'users', UsersModelViewSets, basename='users')

# instance urlpatterns.
urlpatterns = []
# populate instance.
urlpatterns += router.urls

# print('URLPATTERNS:', urlpatterns)
# for url in urlpatterns:
#     print(url)