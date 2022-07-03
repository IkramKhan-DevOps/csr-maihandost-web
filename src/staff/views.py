from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic import (
    TemplateView
)

staff_decorators = [login_required, user_passes_test(lambda u: u.is_superuser)]


@method_decorator(staff_decorators, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'admins/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        return context
