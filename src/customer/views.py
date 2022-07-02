import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, ListView, DeleteView, CreateView, UpdateView, DetailView
from notifications.signals import notify

from src.admins.filters import OrderFilter
from src.admins.models import Order, GiftCard
from src.api.models import AlertMessage


@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'customer/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        return context


""" ORDERS """


@method_decorator(login_required, name='dispatch')
class OrderCreateView(CreateView):
    model = Order
    fields = [
        'receiver_first_name', 'receiver_last_name',
        'receiver_phone_number', 'receiver_email', 'receiver_country',
    ]
    template_name = 'customer/order_create_form.html'

    def dispatch(self, request, *args, **kwargs):
        get_object_or_404(GiftCard, pk=kwargs['pk'])
        return super(OrderCreateView, self).dispatch(request)

    def form_valid(self, form):
        gift_card = get_object_or_404(GiftCard, pk=self.kwargs['pk'])
        form.instance.sender=self.request.user
        form.instance.gift_card = gift_card
        form.instance.total_amount = gift_card.price
        return super(OrderCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('payments:create_checkout_session', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class OrderListView(ListView):
    paginate_by = 100
    template_name = 'customer/order_list.html'

    def get_queryset(self):
        return Order.objects.filter(sender=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data(**kwargs)
        object_filter = OrderFilter(self.request.GET, queryset=self.get_queryset())
        context['object_filter_form'] = object_filter.form

        paginator = Paginator(object_filter.qs, 50)
        page_number = self.request.GET.get('page')
        user_page_object = paginator.get_page(page_number)

        context['object_list'] = user_page_object
        return context


@method_decorator(login_required, name='dispatch')
class OrderUpdateView(UpdateView):
    model = Order
    fields = '__all__'
    template_name = 'customer/order_form.html'
    success_url = reverse_lazy('admins:order-list')

    def get_object(self, queryset=None):
        return get_object_or_404(Order.objects.filter(sender=self.request.user), pk=self.kwargs['pk'])


@method_decorator(login_required, name='dispatch')
class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'customer/order_confirm_delete.html'
    success_url = reverse_lazy('admins:order-list')

    def get_object(self, queryset=None):
        return get_object_or_404(Order.objects.filter(sender=self.request.user), pk=self.kwargs['pk'])


@method_decorator(login_required, name='dispatch')
class OrderDetailView(DetailView):
    model = Order
    template_name = 'customer/order_detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Order.objects.filter(sender=self.request.user), pk=self.kwargs['pk'])


