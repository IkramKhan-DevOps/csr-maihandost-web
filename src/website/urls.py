from django.urls import path
from django.views.generic import TemplateView

from src.website.views import HomeView, OrderCreateView, GiftView

app_name = 'website'
urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('order/gift/<int:pk>/', OrderCreateView.as_view(), name='order_add'),
    path('gift/', GiftView.as_view(), name='gifts'),

]
