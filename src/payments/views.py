import stripe
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from core import settings
from src.admins.bll import calculate_charges_on_order
from src.admins.models import GiftCard, Order


@csrf_exempt
def create_checkout_session(request, pk):

    # GET INFO
    domain_url = settings.DOMAIN_URL
    order = get_object_or_404(Order, pk=pk)
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # BLL
    order_name = "Custom Offer" if order.is_customized else order.gift_card.name
    payable, tax, charges = calculate_charges_on_order(order.total_amount)

    # SAVE INFO
    order.tax_charges = tax
    order.fees_charges = charges
    order.payable_amount = payable
    order.save()

    # CALL PAYMENTS
    session = stripe.checkout.Session.create(
        line_items=[{
            'name': order_name,
            'quantity': 1,
            'currency': 'usd',
            'amount': int(str(int(order.payable_amount))+"00"),
        }],
        mode='payment',
        success_url=request.build_absolute_uri(
            reverse('payments:success')
        ) + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri(reverse('payments:cancel')),
    )

    order.stripe_pay_id = session.id
    order.save()

    return redirect(session.url, code=303)


class SuccessView(TemplateView):
    template_name = 'payments/success.html'

    def get(self, request, *args, **kwargs):
        session_id = request.GET.get('session_id')
        if session_id is None:
            return HttpResponseNotFound()

        stripe.api_key = settings.STRIPE_SECRET_KEY
        session = stripe.checkout.Session.retrieve(session_id)

        order = get_object_or_404(Order, stripe_pay_id=session_id)
        order.status = 'pai'
        order.save()

        context = {
            'order': order
        }

        # TODO: Generate emails + generate messages + everything

        return render(request, self.template_name, context=context)


class CancelledView(TemplateView):
    template_name = 'payments/cancelled.html'
