from django.urls import path, include
from rest_framework.routers import DefaultRouter
from homeserver.views.create import HomeServerViewSet,LoginHomeServerViewset

router = DefaultRouter()
router.register('homeservers', HomeServerViewSet, basename='homeserver')
router.register('login', LoginHomeServerViewset, basename='login')

urlpatterns = [
    path('', include(router.urls)),
]