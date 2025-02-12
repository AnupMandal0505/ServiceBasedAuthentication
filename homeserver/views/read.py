from rest_framework import viewsets, status
from rest_framework.response import Response
from homeserver.serializers.home_server_serializers import HomeServerSerializer
from homeserver.views.base_auth_token import BaseAuth

class HomeServerViewSet(BaseAuth): 
    def list(self, request):
        home_server_user = request.home_server_user
        serializer = HomeServerSerializer(home_server_user, many=True)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)