from django.views.generic import TemplateView

from accounts.forms import LoginForm


class LoginTemplateView(TemplateView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ECommerce | Login'
        context['form'] = LoginForm()
        return context