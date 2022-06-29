from datetime import datetime
from dateutil.relativedelta import *
from django.core.paginator import Paginator
from django.utils import timezone

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.db import transaction
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import (
    TemplateView, ListView, DeleteView, DetailView, UpdateView, CreateView
)
from notifications.signals import notify

# from faker_data import initialization
from src.accounts.models import User
from src.admins.filters import UserFilter, OrderFilter
from src.admins.models import Order, GiftCard

admin_decorators = [login_required, user_passes_test(lambda u: u.is_superuser)]


@method_decorator(admin_decorators, name='dispatch')
class DashboardView(TemplateView):
    """
    Registrations: Today, Month, Year (PAID/UNPAID)
    Subscriptions: Today, Month, Year (TYPES)
    Withdrawals  : Today, Month, Year (CALCULATE)
    """
    template_name = 'admins/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        # context = calculate_statistics(context)
        # initialization(init=False, mid=False, end=False)
        return context


""" USERS """


@method_decorator(admin_decorators, name='dispatch')
class UserListView(ListView):
    model = User
    template_name = 'admins/user_list.html'
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        user_filter = UserFilter(self.request.GET, queryset=User.objects.filter())
        context['user_filter_form'] = user_filter.form

        paginator = Paginator(user_filter.qs, 50)
        page_number = self.request.GET.get('page')
        user_page_object = paginator.get_page(page_number)

        context['user_list'] = user_page_object
        return context


@method_decorator(admin_decorators, name='dispatch')
class UserDetailView(DetailView):
    model = User
    template_name = 'admins/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        return context


@method_decorator(admin_decorators, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = [
        'profile_image', 'first_name', 'last_name',
        'email', 'username', 'phone_number', 'is_active'
    ]
    template_name = 'admins/user_update_form.html'

    def get_success_url(self):
        return reverse('admins:user-detail', kwargs={'pk': self.object.pk})


@method_decorator(admin_decorators, name='dispatch')
class UserPasswordResetView(View):

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = AdminPasswordChangeForm(user=user)
        return render(request, 'admins/admin_password_reset.html', {'form': form})

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = AdminPasswordChangeForm(data=request.POST, user=user)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, f"{user.get_full_name()}'s password changed successfully.")
        return render(request, 'admins/admin_password_reset.html', {'form': form})


""" ORDERS VIEWS """


@method_decorator(admin_decorators, name='dispatch')
class OrderListView(ListView):
    queryset = Order.objects.all()
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data(**kwargs)
        object_filter = OrderFilter(self.request.GET, queryset=Order.objects.filter())
        context['object_filter_form'] = object_filter.form

        paginator = Paginator(object_filter.qs, 50)
        page_number = self.request.GET.get('page')
        user_page_object = paginator.get_page(page_number)

        context['object_list'] = user_page_object
        return context


@method_decorator(admin_decorators, name='dispatch')
class OrderUpdateView(UpdateView):
    model = Order
    fields = '__all__'
    success_url = reverse_lazy('admins:order-list')


@method_decorator(admin_decorators, name='dispatch')
class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('admins:order-list')


@method_decorator(admin_decorators, name='dispatch')
class OrderDetailView(DetailView):
    model = Order


""" GIFTS """


@method_decorator(admin_decorators, name='dispatch')
class GiftCardListView(ListView):
    queryset = GiftCard.objects.all()


@method_decorator(admin_decorators, name='dispatch')
class GiftCardCreateView(CreateView):
    model = GiftCard
    fields = '__all__'
    success_url = reverse_lazy('admins:gift-card-list')


@method_decorator(admin_decorators, name='dispatch')
class GiftCardUpdateView(UpdateView):
    model = GiftCard
    fields = '__all__'
    success_url = reverse_lazy('admins:gift-card-list')


@method_decorator(admin_decorators, name='dispatch')
class GiftCardDeleteView(DeleteView):
    model = GiftCard
    success_url = reverse_lazy('admins:gift-card-list')
