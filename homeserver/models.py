from django.db import models
import uuid
from django.contrib.auth.hashers import make_password


class HomeServer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    api_key = models.CharField(max_length=255, unique=True)
    max_users = models.IntegerField(default=5)  # Initial user limit
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=100, unique=True)
    # Username and Encrypted Password
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)  # Store hashed password

    # Date and Time Information
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)


# Method to set password (encryption)
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    # Method to check password (validation)
    def check_password(self, raw_password):
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.password)
    

    def __str__(self):
        return f"{self.name} (Max Users: {self.max_users})"


class UserAccount(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    home_server = models.ForeignKey(HomeServer, on_delete=models.CASCADE)
    pass_key = models.CharField(max_length=255, unique=True)
    is_on_hold = models.BooleanField(default=False)  # Hold status

    def __str__(self):
        return f"{self.username} ({'On Hold' if self.is_on_hold else 'Active'})"


class RequestLog(models.Model):
    REQUEST_TYPES = [('increase_limit', 'Increase Limit'), ('user_hold', 'User Hold')]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    home_server = models.ForeignKey(HomeServer, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES, default='increase_limit')
    note = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.home_server.name} - {self.request_type} at {self.created_at}"
