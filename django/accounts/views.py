from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView 
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from .models import Account
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
    # model = Account
    # fields = ['id', 'username', 'first_name', 'last_name', 'email']
    success_url = reverse_lazy('my-account')

    def get_object(self):
        print(self.request)
        return Account.objects.get(pk=self.request.user.id)

    def post(self, request, *args):
        form = self.form_class(data=request.POST)
        
        print('form valid?')
        print(form.is_valid())
        self.object = self.get_object()

        if form.is_valid():
            print('form valid....')
            form.save()
            messages.success(request, 'Account Updated')
            return self.form_valid(form)

       
        # return self.form_invalid(form)

        return redirect(self.success_url)

    def form_valid(self, form):
        print('form is valid....')
        form.save()
        return super().form_valid(form)

