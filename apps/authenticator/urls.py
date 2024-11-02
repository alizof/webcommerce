from django.urls import include, path
from rest_framework import routers

from .views import UserViewSet, SignUpUserView


router = routers.DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
  path('', include(router.urls)),
  path('api/v1/auth/register/', SignUpUserView.as_view(), name='created-user'),
]
