from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from .forms import UpdateAccountForm


class AccountSettingsView(TemplateView):
    template_name = 'accounts/settings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_account"] = self.request.user
        return context


class AccountUpateView(FormView):
    form_class = UpdateAccountForm
    success_url = reverse_lazy('my-account')

    def post(self, request, *args):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            messages.success(request, 'Account Updated')

        return super().post(request, *args)
