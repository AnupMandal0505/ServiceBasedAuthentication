from django.contrib import admin
from django.http import HttpResponse
import csv
from homeserver.models.home_server import HomeServer
from homeserver.models.account_info import UserAccount, RequestLog  # Import models
from django.urls import path


# Register the model with admin panel
@admin.register(HomeServer)
class HomeServerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'phone_number', 'max_users', 'is_active', 'created_at')  # Columns in admin list
    search_fields = ('company_name', 'email', 'full_name', 'phone_number')  # Searchable fields
    list_filter = ('is_active', 'max_users', 'created_at')  # Filters on right sidebar
    readonly_fields = ('created_at', 'last_updated')  # Read-only fields

    fieldsets = (
        ("Basic Information", {
            'fields': ('company_name', 'full_name', 'password', 'is_active')
        }),
        ("Contact Details", {
            'fields': ('email', 'phone_number', 'address')
        }),
        ("Server Details", {
            'fields': ('max_users',)
        }),
        ("Timestamps", {
            'fields': ('created_at', 'last_updated')
        }),
    )

    actions = ['export_as_csv']  # Add CSV export button

    def export_as_csv(self, request, queryset):
        """Export selected data as CSV"""
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=home_servers.csv'
        
        writer = csv.writer(response)
        writer.writerow(['Company_name', 'Email', 'Phone', 'full_name', 'Max Users', 'Active', 'Created At'])
        
        for obj in queryset:
            writer.writerow([obj.company_name, obj.email, obj.phone_number, obj.full_name, obj.max_users, obj.is_active, obj.created_at])
        
        return response

    export_as_csv.short_description = "Download CSV (selected records)"



# 🔹 Register UserAccount Admin
@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('phone', 'home_server', 'is_on_hold')
    search_fields = ('phone', 'home_server__name')
    list_filter = ('is_on_hold',)
    readonly_fields = ('id',)
    
    fieldsets = (
        ("Account Info", {'fields': ('phone', 'pass_key', 'home_server')}),
        ("Status", {'fields': ('is_on_hold',)}),
    )

    actions = ['export_as_csv']  # Add CSV export button


    def export_as_csv(self, request,queryset):
        """Generate CSV file for UserAccounts"""
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=user_accounts.csv'

        writer = csv.writer(response)
        writer.writerow(['phone', 'Home Server', 'On Hold'])

        for obj in queryset:
            writer.writerow([obj.phone, obj.home_server.name, obj.is_on_hold])

        return response
    
    export_as_csv.short_description = "Download CSV (selected records)"


   


# 🔹 Register RequestLog Admin
@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):
    list_display = ('home_server', 'request_type', 'status', 'created_at')
    search_fields = ('home_server__name', 'request_type')
    list_filter = ('request_type', 'status')
    readonly_fields = ('id', 'created_at')

    fieldsets = (
        ("Request Details", {'fields': ('home_server', 'request_type', 'note')}),
        ("Status", {'fields': ('status',)}),
        ("Timestamps", {'fields': ('created_at',)}),
    )

    actions = ['export_as_csv']  # Add CSV export button


    def export_as_csv(self, request,queryset):
        """Generate CSV file for Request Logs"""
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=request_logs.csv'

        writer = csv.writer(response)
        writer.writerow(['Home Server', 'Request Type', 'Note', 'Status', 'Created At'])

        for obj in queryset:
            writer.writerow([obj.home_server.name, obj.request_type, obj.note, obj.status, obj.created_at])

        return response

    export_as_csv.short_description = "Download CSV (selected records)"
