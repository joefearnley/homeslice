from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import LoginForm, SignupForm
from django.views.generic import View
from django.views.generic.edit import FormView


class SignupView(FormView):
    template_name = 'signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('bookmark_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super(SignupView, self).form_valid(form)


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('bookmark_list')

    def form_valid(self, form):
        user = authenticate(
            username=self.request.POST['email'], 
            password=self.request.POST['password']
        )
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
