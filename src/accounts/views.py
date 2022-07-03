from allauth.account.models import EmailAddress
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.views.generic import View
from django.contrib.auth import logout, login
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework import permissions, status
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from rest_framework.response import Response
from rest_framework.views import APIView
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from core.settings import GOOGLE_CALLBACK_ADDRESS
from src.accounts.forms import UserProfileForm
from src.accounts.models import User
from src.accounts.serializers import CustomRegisterAccountSerializer
from src.accounts.tokens import account_activation_token


class LoginView(View):

    def post(self, request):
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_superuser or user.is_staff:
                login(request, user)
                if 'next' in request.POST:
                    return HttpResponseRedirect(reverse('next'))
                else:
                    return HttpResponseRedirect(reverse('admins:dashboard'))
            else:
                messages.error(
                    request, "You are not allowed to access administration. Need help? Please consult admin"
                )
        return render(request, 'admins/login.html', {'form': form})

    def get(self, request):
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.is_staff:
                return redirect('admins:dashboard')
            else:
                logout(request)
                messages.error(
                    request, "You are not allowed to access administration. Need help? Please consult admin"
                )
                return redirect('accounts:administration-login')

        form = AuthenticationForm()
        return render(request=request, template_name='admins/login.html', context={'form': form})


@method_decorator(login_required, name='dispatch')
class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('account_login')


@method_decorator(login_required, name='dispatch')
class CrossAuthView(View):

    def get(self, request):
        if request.user.is_superuser or request.user.is_staff:
            if request.user.is_superuser:
                return redirect('admins:dashboard')
            else:
                return redirect('staff:dashboard')
        else:
            return redirect('customer:dashboard')


@method_decorator(login_required, name='dispatch')
class UserUpdateView(View):

    def get(self, request):
        form = UserProfileForm(instance=request.user)
        context = {'form': form}
        return render(request, template_name='accounts/user_update_form.html', context=context)

    def post(self, request):
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            messages.success(request, "Your profile updated successfully")
            form.save(commit=True)
        context = {'form': form}
        return render(request, template_name='accounts/user_update_form.html', context=context)


class GoogleLoginView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = GOOGLE_CALLBACK_ADDRESS


class FacebookLoginView(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class CustomRegisterAccountView(APIView):
    serializer_class = CustomRegisterAccountSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = {}
        status_code = status.HTTP_400_BAD_REQUEST
        serializer = CustomRegisterAccountSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            EmailAddress.objects.create(user=user, email=user.email, primary=True, verified=False)
            data = {'success': 'Account created successfully'}
            status_code = status.HTTP_201_CREATED

            current_site = get_current_site(request)
            mail_subject = 'Activate your Maihan Dost account.'
            message = render_to_string('accounts/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = user.email
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()

        else:
            data = serializer.errors
        return Response(data=data, status=status_code)


def view_activate(request, uidb64, token):
    try:

        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        try:
            email_account = EmailAddress.objects.get(user=user)
        except EmailAddress.DoesNotExist:
            email_account = EmailAddress.objects.create(
                user=user, email=user.email, primary=True
            )
        email_account.verified = True
        email_account.save()

        user.save()
        # return redirect('home')
        return render(
            request,
            template_name='accounts/signup_confirm.html',
            context={
                'message': 'Thank you for your email confirmation, GOOD LUCK! help the needy, make your '
                           'profile, be a reason of someone to smile and become a HERO.'
            }
        )
    else:
        return render(
            request,
            template_name='accounts/signup_confirm.html',
            context={'message': 'unable to activate account because the activation link is invalid'}
        )
