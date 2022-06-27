import stripe
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from core import settings


@csrf_exempt
def create_checkout_session(request, pk):
    domain_url = settings.DOMAIN_URL
    # filing = get_object_or_404(Filing, pk=pk)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    session = stripe.checkout.Session.create(
        line_items=[{
            'name': 'Gold Gift',
            'quantity': 1,
            'currency': 'gbp',
            'amount': 3500,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(
            reverse('payments:success')
        ) + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri(reverse('payments:cancel')),
    )
    # filing.stripe_payment_intent = session.id
    # filing.save()

    return redirect(session.url, code=303)


class SuccessView(TemplateView):
    template_name = 'payments/success.html'

    def get(self, request, *args, **kwargs):
        session_id = request.GET.get('session_id')
        if session_id is None:
            return HttpResponseNotFound()

        stripe.api_key = settings.STRIPE_SECRET_KEY
        session = stripe.checkout.Session.retrieve(session_id)

        # filing = get_object_or_404(Filing, stripe_payment_intent=session_id)
        # filing.is_paid = True
        # filing.is_active = False
        # filing.save()

        return render(request, self.template_name)


class CancelledView(TemplateView):
    template_name = 'payments/cancelled.html'
