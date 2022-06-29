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


class OrderCreateView(CreateView):
    model = Order
    fields = [
        'sender_first_name', 'sender_last_name', 'sender_phone_number', 'sender_email', 'sender_country',
        'receiver_first_name', 'receiver_last_name', 'receiver_phone_number', 'receiver_email', 'receiver_country',
    ]
    template_name = 'website/order.html'

    def dispatch(self, request, *args, **kwargs):
        get_object_or_404(GiftCard, pk=kwargs['pk'])
        return super(OrderCreateView, self).dispatch(request)

    def form_valid(self, form):
        gift_card = get_object_or_404(GiftCard, pk=self.kwargs['pk'])
        form.instance.gift_card = gift_card
        form.instance.total_amount = gift_card.price
        return super(OrderCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('payments:create_checkout_session', kwargs={'pk': self.object.pk})


class GiftView(TemplateView):
    template_name = 'website/gifts.html'

    def get_context_data(self, **kwargs):
        context = super(GiftView, self).get_context_data(**kwargs)
        context['gift_cards'] = GiftCard.objects.all()[0:9]
        return context
