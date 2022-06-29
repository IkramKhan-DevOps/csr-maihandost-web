import django_filters
from django.forms import TextInput

from src.accounts.models import User
from src.admins.models import Order


class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(widget=TextInput(attrs={'placeholder': 'username'}), lookup_expr='icontains')
    first_name = django_filters.CharFilter(widget=TextInput(attrs={'placeholder': 'first name'}), lookup_expr='icontains')
    last_name = django_filters.CharFilter(widget=TextInput(attrs={'placeholder': 'last name'}), lookup_expr='icontains')
    email = django_filters.CharFilter(widget=TextInput(attrs={'placeholder': 'email'}), lookup_expr='icontains')

    class Meta:
        model = User
        fields = {}


class OrderFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(widget=TextInput(attrs={'placeholder': 'ID'}), lookup_expr='icontains')
    sender_email = django_filters.CharFilter(widget=TextInput(attrs={'placeholder': 'Sender Email'}), lookup_expr='icontains')
    receiver_email = django_filters.CharFilter(widget=TextInput(attrs={'placeholder': 'Receiver Email'}), lookup_expr='icontains')

    class Meta:
        model = Order
        fields = {
            'status', 'is_active'
        }

