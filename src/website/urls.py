from django.urls import path
from django.views.generic import TemplateView

from src.website.views import (
    HomeView, GiftView,
    PrivacyPolicyView, TermsView
)

app_name = 'website'
urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('gift/', GiftView.as_view(), name='gifts'),

    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacy-policy'),
    path('terms-and-conditions/', TermsView.as_view(), name='terms-and-conditions'),

]
