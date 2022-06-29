from django.urls import path
from django.views.generic import TemplateView

from src.website.views import (
    HomeView, OrderCreateView, GiftView,
    PrivacyPolicyView, TermsView
)

app_name = 'website'
urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('order/gift/<int:pk>/', OrderCreateView.as_view(), name='order_add'),
    path('gift/', GiftView.as_view(), name='gifts'),

    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacy-policy'),
    path('terms-and-conditions/', TermsView.as_view(), name='terms-and-conditions'),

]
