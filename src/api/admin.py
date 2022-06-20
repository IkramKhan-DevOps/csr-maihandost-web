from django.contrib import admin
from django.utils.html import format_html

from .models import (
    AlertMessage
)


class AlertMessageAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 'title', 'alert_type', 'created_on', 'is_active'
    ]
    list_filters = ['alert_type']


admin.site.register(AlertMessage, AlertMessageAdmin)

