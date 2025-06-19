from django.views.generic import TemplateView

from accounts.forms import UserChangeForm


class ProfileTemplateView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ECommerce | Profile'
        context['current_user'] = self.request.user
        context['form'] = UserChangeForm()
        return context