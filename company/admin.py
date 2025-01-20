from django.contrib import admin
from .models import Company, CompanyServiceSubscription
from django.utils.translation import gettext_lazy as _  # For internationalization

class CompanyAdmin(admin.ModelAdmin):
    # Define fieldsets to organize fields in the admin panel
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'phone_number', 'address', 'username', 'password')
        }),
        (_('Status Information'), {
            'fields': ('is_active',),
            'classes': ('collapse',)  # This makes the "Status Information" section collapsible
        }),
        (_('Date Information'), {
            'fields': ('created_at', 'last_updated'),
            'classes': ('collapse',)  # This makes the "Date Information" section collapsible
        }),
    )

    # Configure display in the admin list view
    list_display = ('name', 'email', 'username', 'is_active', 'created_at')
    search_fields = ('name', 'username', 'email')
    list_filter = ('is_active',)
    readonly_fields = ('created_at', 'last_updated')  # These fields should be read-only

    def save_model(self, request, obj, form, change):
        # Ensure password is hashed when saving
        if 'password' in form.changed_data:
            obj.set_password(obj.password)  # Hash the password
        super().save_model(request, obj, form, change)

admin.site.register(Company, CompanyAdmin)





class CompanyServiceSubscriptionAdmin(admin.ModelAdmin):
    # Define fieldsets to organize fields in the admin panel
    fieldsets = (
        (None, {
            'fields': ('company', 'number_of_accounts', 'subscription_start_date', 'subscription_end_date')
        }),
        (_('Subscription Status'), {
            'fields': ('is_active',),
            'classes': ('collapse',)  # This makes the "Subscription Status" section collapsible
        }),
    )

    # Configure display in the admin list view
    list_display = ('company', 'number_of_accounts', 'subscription_start_date', 'subscription_end_date', 'is_active')
    search_fields = ('company__name',)
    list_filter = ('is_active',)

admin.site.register(CompanyServiceSubscription, CompanyServiceSubscriptionAdmin)
