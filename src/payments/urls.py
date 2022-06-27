from django.urls import path
from .views import (
    create_checkout_session, SuccessView, CancelledView
)

app_name = 'payments'
urlpatterns = [

    path('create-checkout-session/<int:pk>/', create_checkout_session, name='create_checkout_session'),

    path('success/', SuccessView.as_view(), name='success'),
    path('cancelled/', CancelledView.as_view(), name='cancel'),
]
