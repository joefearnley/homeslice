from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
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


class AccountUpateView(UpdateView):
    # template_name = 'accounts/settings.html'
    form_class = UpdateAccountForm
    success_url = reverse_lazy('my-account')

    def post(self, request, *args):
        form = self.form_class(data=request.POST)


        print(form.is_valid())

        if form.is_valid():
            print('form valid....')
            messages.success(request, 'Account Updated')

        print('redirecting.....')

        return redirect(self.success_url)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

