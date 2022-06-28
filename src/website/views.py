import os
from core import settings
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView, CreateView


def handler404(request, exception, template_name='404.html'):
    return render(request, template_name)


class HomeView(TemplateView):
    template_name = 'website/home.html'


class OrderCreateView(CreateView):
    template_name = 'website/order.html'


class GiftView(TemplateView):
    template_name = 'website/gifts.html'
