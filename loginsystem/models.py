from django.db import models
import uuid
from django.contrib.auth.hashers import make_password
from company.models import CompanyServiceSubscription


class LoginSystem(models.Model):
    # Unique ID for the user
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Basic user fields
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Store hashed password
    is_active = models.BooleanField(default=True)

    # Role field
    ROLE_CHOICES = (
        ('GM', 'Gm'),
        ('PA', 'Pa'),
    )
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='PA'
    )

    # Tracking who created the user
    created_by = models.ForeignKey(
        CompanyServiceSubscription,  # Reference to the same User model
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_users',  # Reverse relationship
        help_text="The user who created this user"
    )

    # Date fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Method to set password (encryption)
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    # Method to check password (validation)
    def check_password(self, raw_password):
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

    # class Meta:
    #     verbose_name = "User"
    #     verbose_name_plural = "Users"
