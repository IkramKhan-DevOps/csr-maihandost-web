import notifications.urls
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from dj_rest_auth.registration.views import VerifyEmailView
from django.views.static import serve

from src.accounts.views import GoogleLoginView, FacebookLoginView, CustomRegisterAccountView

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from .settings import DEBUG, STATIC_ROOT, MEDIA_ROOT
from src.website.views import handler404

handler404 = handler404
urlpatterns = [

    # ADMIN/ROOT APPLICATION
    path('admin/', admin.site.urls),
    path('', include('src.website.urls', namespace='website')),

    path('admins/', include('src.admins.urls', namespace='admins')),
    path('customer/', include('src.customer.urls', namespace='customer')),
    path('accounts/', include('src.accounts.urls', namespace='accounts')),
    path('accounts/', include('allauth.urls')),

    path('payments/', include('src.payments.urls', namespace='payments')),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),

]

# urlpatterns += [
#     path(
#         'reset/password/', auth_views.PasswordResetView.as_view(
#             template_name="accounts/reset_password.html"
#         ), name='reset_password'
#     ),
#     path(
#         'reset/password/sent/',
#         auth_views.PasswordResetDoneView.as_view(
#             template_name="accounts/password_reset_sent.html"
#         ), name='password_reset_done'
#     ),
#     path(
#         'reset/<uidb64>/<token>',
#         auth_views.PasswordResetConfirmView.as_view(
#             template_name="accounts/password_reset_form.html"
#         ), name='password_reset_confirm'
#     ),
#     path(
#         'reset/password/complete/',
#         auth_views.PasswordResetCompleteView.as_view(
#             template_name="accounts/password_reset_done.html"
#         ), name='password_reset_complete'
#     ),
# ]
#
# urlpatterns += [
#     re_path(r'^account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
#     re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(), name='account_confirm_email'),
# ]
#
# urlpatterns += [
#     path('auth/', include('dj_rest_auth.urls')),
#     path('auth/registration/', CustomRegisterAccountView.as_view(), name='account_create_new_user'),
#     path('auth/google/', GoogleLoginView.as_view(), name='google-login-view'),
#     path('auth/facebook/', FacebookLoginView.as_view(), name='facebook-login-view'),
# ]

urlpatterns += [
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
]
