from django.db import models
import uuid
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token as DefaultTokenModel



class HomeServer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, unique=True)
    max_users = models.IntegerField(default=5) 
    address = models.TextField()
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255) 

    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.company_name




class HomeServerToken(DefaultTokenModel):
    user = models.OneToOneField(HomeServer, on_delete=models.CASCADE, related_name='auth_token')