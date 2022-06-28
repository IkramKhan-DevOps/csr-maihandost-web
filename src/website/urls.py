from django.urls import path
from django.views.generic import TemplateView

from src.website.views import HomeView, OrderView

app_name = 'website'
urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('go/fast/', OrderView.as_view(), name='go_fast'),
    path('gift/', OrderView.as_view(), name='gifts'),

]
