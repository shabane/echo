from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import LinkViewSet, ServerViewSet


router = DefaultRouter()
router.register('users', LinkViewSet, basename='users')
router.register('server', ServerViewSet, basename='server')


urlpatterns = [
    path('', include(router.urls))
]
