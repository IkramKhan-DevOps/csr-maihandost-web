import os

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from core import settings


def handler404(request, exception, template_name='404.html'):
    return render(request, template_name)


class HomeView(TemplateView):
    template_name = 'website/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context


class OrderView(TemplateView):
    template_name = 'website/order.html'

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        return context


class GiftView(TemplateView):
    template_name = 'website/gifts.html'

    def get_context_data(self, **kwargs):
        context = super(GiftView, self).get_context_data(**kwargs)
        return context

