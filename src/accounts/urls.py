from django.urls import path

from .views import LoginView, LogoutView, view_activate, CrossAuthView, UserUpdateView

app_name = 'accounts'
urlpatterns = [
    path('admin/login/', LoginView.as_view(), name='administration-login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/change/', UserUpdateView.as_view(), name='user-change'),

    path('cross-auth/', CrossAuthView.as_view(), name='cross-auth')
    # path('activate/<uidb64>/<token>/', view_activate, name='activate'),
]
