from django.views.generic import TemplateView

from accounts.forms import UserCreationForm


class RegisterTemplateView(TemplateView):
    template_name = 'register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ECommerce | Register'
        context['form'] = UserCreationForm()
        return context