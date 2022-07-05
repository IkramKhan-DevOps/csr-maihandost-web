from django.urls import path

from .views import (
    DashboardView,
    OrderListView, OrderCreateView, OrderUpdateView, OrderDetailView,
    OrderDeleteView, OrderInvoiceView
)

app_name = 'customer'
urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
]

urlpatterns += [
    path('order/', OrderListView.as_view(), name='order-list'),
    path('order/add/<int:pk>/', OrderCreateView.as_view(), name='order-add'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('order/<int:pk>/update/', OrderUpdateView.as_view(), name='order-update'),
    path('order/<int:pk>/invoice/', OrderInvoiceView.as_view(), name='order-invoice'),
    path('order/<int:pk>/delete/', OrderCreateView.as_view(), name='order-delete'),
]
