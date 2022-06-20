import os

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views import View

from core import settings


def handler404(request, exception, template_name='404.html'):
    return render(request, template_name)


class HomeView(View):

    def get(self, request):
        context = {}
        return render(request, 'website/home.html', context)

