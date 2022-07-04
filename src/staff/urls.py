from django.urls import path
from .views import (
    DashboardView,
    OrderSearchView, OrderDetailView, OrderDetailInvoiceView
)

app_name = 'staff'
urlpatterns = [

    path('', DashboardView.as_view(), name='dashboard'),
    path('search/', OrderSearchView.as_view(), name='order-search'),
    path('order/<uuid:tx_id>/', OrderDetailView.as_view(), name='order-detail'),
    path('order/<uuid:tx_id>/invoice/', OrderDetailInvoiceView.as_view(), name='order-invoice')

]
