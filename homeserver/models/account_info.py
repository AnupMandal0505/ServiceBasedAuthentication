from django.db import models
from .home_server import HomeServer
import uuid


class UserAccount(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    home_server = models.ForeignKey(HomeServer, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100, unique=True)
    pass_key = models.CharField(max_length=255, unique=True)
    is_on_hold = models.BooleanField(default=False)  # Hold status

    def __str__(self):
        return f"{self.phone} ({'On Hold' if self.is_on_hold else 'Active'})"

  

class RequestLog(models.Model):
    REQUEST_TYPES = [('increase_limit', 'Increase Limit'), ('user_hold', 'User Hold')]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    home_server = models.ForeignKey(HomeServer, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES, default='increase_limit')
    note = models.TextField(max_length=500)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.home_server.name} - {self.request_type} at {self.created_at}"