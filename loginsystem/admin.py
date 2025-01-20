from django.contrib import admin
from .models import LoginSystem
from django.utils.translation import gettext_lazy as _

class LoginSystemAdmin(admin.ModelAdmin):
    # Define the fieldsets for the User model in the admin panel
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password', 'is_active')
        }),
        (_('Role Information'), {
            'fields': ('role',)
        }),
        (_('User Creation Information'), {
            'fields': ('created_by', 'created_at', 'updated_at'),
            'classes': ('collapse',)  # Optional: This makes this section collapsible
        }),
    )
    
    # Optionally you can also add other configurations like ordering, list_display, etc.
    list_display = ('username', 'email', 'role', 'is_active', 'created_at')
    search_fields = ('username', 'email')
    list_filter = ('is_active', 'role')

    # Define how the password should be displayed (it shouldn't be displayed in the admin interface)
    readonly_fields = ('created_at', 'updated_at')


    def save_model(self, request, obj, form, change):
        # Ensure password is hashed when saving
        if 'password' in form.changed_data:
            obj.set_password(obj.password)  # Hash the password
        super().save_model(request, obj, form, change)
        
admin.site.register(LoginSystem, LoginSystemAdmin)
