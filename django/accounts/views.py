from django.views.generic import TemplateView


class AccountSettingsView(TemplateView):
    template_name = 'accounts/settings.html'


class AccountUpateView(View):
    # 