from django.urls import path, include
from rest_framework.routers import DefaultRouter
from homeserver.views.create import HomeServerViewSet,LoginHomeServerViewset
from homeserver.views.read import AppControlAuth

router = DefaultRouter()
router.register('homeservers', HomeServerViewSet, basename='homeserver')
router.register('login', LoginHomeServerViewset, basename='login')
router.register('app_access', AppControlAuth, basename='app_access')

urlpatterns = [
    path('', include(router.urls)),
]