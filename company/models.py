import uuid
from django.db import models
from django.contrib.auth.hashers import make_password

class Company(models.Model):
    # Unique identifier for the company
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Basic company details
    name = models.CharField(max_length=200, unique=True)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=100, unique=True)

    # Username and Encrypted Password
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)  # Store hashed password

    is_active = models.BooleanField(default=True)

    # Date and Time Information
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    # Method to set password (encryption)
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    # Method to check password (validation)
    def check_password(self, raw_password):
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.name








class CompanyServiceSubscription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="subscriptions")
    # service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="subscriptions")
    number_of_accounts = models.PositiveIntegerField()
    subscription_start_date = models.DateField()
    subscription_end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    # def total_cost(self):
    #     return self.number_of_accounts * self.service.price_per_account

    def __str__(self):
        return self.company.name