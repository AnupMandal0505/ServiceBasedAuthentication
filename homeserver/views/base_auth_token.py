from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import permissions
from homeserver.models.home_server import HomeServerToken
from rest_framework import viewsets


class HomeServerTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            return None
        try:
            token = HomeServerToken.objects.get(key=token.split(' ')[1])
            return (token.user, token)
        except HomeServerToken.DoesNotExist:
            raise AuthenticationFailed('Invalid token')


class HomeServerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return True
        return False
    

class BaseAuth(viewsets.ViewSet):
    authentication_classes = [HomeServerTokenAuthentication]
    permission_classes = [HomeServerPermission]
    def get_home_server_user(self, request):
        return request.user