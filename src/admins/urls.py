from django.urls import path
from .views import (
    DashboardView,
    UserListView, UserPasswordResetView, UserDetailView, UserUpdateView,
    OrderListView, OrderDetailView, OrderUpdateView, OrderDeleteView
)

app_name = 'admins'
urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),

    path('user/', UserListView.as_view(), name='user-list'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user/<int:pk>/change/', UserUpdateView.as_view(), name='user-update'),
    path('user/<int:pk>/password/reset/', UserPasswordResetView.as_view(), name='user-password-reset-view'),

    path('order/', OrderListView.as_view(), name='order-list'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('order/<int:pk>/update/', OrderUpdateView.as_view(), name='order-update'),
    path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),

]
