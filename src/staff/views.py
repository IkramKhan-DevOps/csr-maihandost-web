from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import (
    TemplateView
)

from src.admins.models import Order

staff_decorators = [login_required, user_passes_test(lambda u: u.is_staff)]


@method_decorator(staff_decorators, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'staff/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        return context


@method_decorator(staff_decorators, name='dispatch')
class OrderSearchView(View):
    template_name = 'staff/order_search.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)

    def post(self, request, *args, **kwargs):

        order_id = self.request.POST.get('order_id')
        if order_id:
            order = Order.objects.filter(transaction_id=order_id, status='pai')
            if order:
                order = order[0]

                return redirect('staff:order-detail', order.transaction_id)
            else:
                messages.error(request, "Requested ID: doesn't exists with an active record")
        else:
            messages.error(request, "Please provide transaction ID")
        return render(request, template_name=self.template_name)


# TODO: use for both staff and admins
@method_decorator(staff_decorators, name='dispatch')
class OrderDetailView(View):
    template_name = 'staff/order_detail.html'

    def get(self, request, tx_id, *args, **kwargs):
        order = get_object_or_404(Order.objects.filter(status='pai'), transaction_id=tx_id)
        context = {'object': order}
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, tx_id, *args, **kwargs):
        order = get_object_or_404(Order.objects.filter(status='pai'), transaction_id=tx_id)
        order.status = 'com'
        order.closed_at = timezone.now()
        order.closed_by = request.user
        order.save()

        messages.success(request, "Order confirmed and closed successfully")
        if request.user.is_superuser:
            return redirect('admins:order-detail', order.pk)
        return redirect('staff:order-search')
