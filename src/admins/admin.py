from django.contrib import admin
from .models import (
    Country, GiftCard, Order
)


class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_available_for_sender', 'is_available_for_receiver', 'is_active']


class GiftCardAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'sender_email', 'receiver_email', 'total_amount', 'payable_amount',
        'gift_card', 'status', 'created_on'
    ]


admin.site.register(Country)
admin.site.register(GiftCard)
admin.site.register(Order)
