from django import forms
from django.forms import inlineformset_factory

from src.admins.models import Order


class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']
