from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from .models import Account
from .forms import UpdateAccountForm, DeleteAccountForm


class AccountSettingsView(TemplateView):
    template_name = 'accounts/settings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_account'] = self.request.user
        context['update_account_form'] = UpdateAccountForm(instance=self.request.user)
        context['delete_account_form'] = DeleteAccountForm(instance=self.request.user)
        return context


class AccountUpateView(UpdateView):
    form_class = UpdateAccountForm
    success_url = reverse_lazy('my-account')

    def get_object(self):
        return Account.objects.get(pk=self.request.user.id)

    def post(self, request, *args):
        form = self.form_class(data=request.POST, instance = request.user)

        # self.object = self.get_object()

        if form.is_valid():
            form.save()
            messages.success(request, 'Account Updated')
        else :
            messages.error(request, form.errors)

        return redirect(self.success_url)

    # def form_invalid(self, form):
    #     return super().form_valid(form)

    # def form_valid(self, form):
    #     print('form is valid....')
    #     form.save()
    #     return super().form_valid(form)

