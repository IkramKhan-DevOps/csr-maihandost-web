import os

from django.urls import reverse_lazy

from core import settings
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView, CreateView

from src.admins.models import GiftCard, Order


def handler404(request, exception, template_name='404.html'):
    return render(request, template_name)


class HomeView(TemplateView):
    template_name = 'website/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['gift_cards'] = GiftCard.objects.all()[0:9]
        return context


class GiftView(TemplateView):
    template_name = 'website/gifts.html'

    def get_context_data(self, **kwargs):
        context = super(GiftView, self).get_context_data(**kwargs)
        context['gift_cards'] = GiftCard.objects.all()[0:9]
        return context


class PrivacyPolicyView(TemplateView):
    template_name = 'website/privacy-policy.html'


class TermsView(TemplateView):
    template_name = 'website/terms-of-use.html'


