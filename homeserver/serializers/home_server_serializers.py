from rest_framework import serializers
from homeserver.models.home_server import HomeServer

class HomeServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeServer
        exclude = ["password","created_at","last_updated","is_active"]
