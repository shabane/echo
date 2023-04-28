from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import LinkViewSet, ServerViewSet, LinkViewReadonly


router = DefaultRouter()
router.register('users/list', LinkViewReadonly, basename='list_users')
router.register('users', LinkViewSet, basename='users')
router.register('server', ServerViewSet, basename='server')


urlpatterns = [
    path('', include(router.urls))
]
