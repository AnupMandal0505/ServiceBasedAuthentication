from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from homeserver.models.home_server import HomeServer,HomeServerToken
from homeserver.serializers.home_server_serializers import HomeServerSerializer
from django.contrib.auth.hashers import make_password,check_password
from homeserver.views.base_auth_token import BaseAuth
    
class HomeServerViewSet(viewsets.ViewSet):
    def create(self, request):
        """Create a new HomeServer entry after checking uniqueness"""

        # Validation: Check unique fields
        if HomeServer.objects.filter(email=request.data.get('email').upper()).exists():
            return Response({"error": "Email is already in use."}, status=status.HTTP_400_BAD_REQUEST)
        
        if HomeServer.objects.filter(phone_number=request.data.get('phone_number').upper()).exists():
            return Response({"error": "Phone number is already in use."}, status=status.HTTP_400_BAD_REQUEST)
        
        if HomeServer.objects.filter(company_name=request.data.get('company_name').upper()).exists():
            return Response({"error": "Company name is already in use."}, status=status.HTTP_400_BAD_REQUEST)

        # Create the HomeServer object
        home_server = HomeServer.objects.create(full_name=request.data.get('full_name').upper(),company_name=request.data.get('company_name').upper(),address=request.data.get('address').upper(),email=request.data.get('email').upper(),phone_number=request.data.get('phone_number').upper(),password=make_password(request.data.get('password')))
        serial=HomeServerSerializer(home_server)
    

        # Response
        return Response({"message": "Home Server created successfully!","data":serial.data}, status=status.HTTP_201_CREATED)



class LoginHomeServerViewset(BaseAuth):
    def create(self, request):
        """Authenticate user and return JWT token"""
        data = request.data
        identifier = data.get('identifier')  # Email, Phone, or Company Name
        password = data.get('password')

        # Check if user exists with email, phone, or company name
        user = HomeServer.objects.filter(
            email=identifier.upper()
        ).first() or HomeServer.objects.filter(
            phone_number=identifier
        ).first()

        if not user:
            return Response({"error": "User not found!"}, status=status.HTTP_404_NOT_FOUND)

        # Validate Password
        if not check_password(password, user.password):
            return Response({"error": "Invalid password!"}, status=status.HTTP_400_BAD_REQUEST)

        # Generate or update token
        if HomeServerToken.objects.filter(user=user).exists():
            HomeServerToken.objects.get(user=user).delete()
        token = HomeServerToken.objects.create(user=user)

        return Response({
            'user': HomeServerSerializer(user, many=False).data,
            'Token': token.key
        }, status=status.HTTP_200_OK)
        