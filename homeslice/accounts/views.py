from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import LoginForm, SignUpForm
from django.views.generic import View
from django.views.generic.edit import FormView


class SignupView(FormView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('bookmark_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super(SignupView, self).form_valid(form)


class LoginView(FormView):
     template_name = 'login.html'
     form_class = LoginForm

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.add_message(request, messages.INFO, 'You are now logged-In, welcome')
    #         return HttpResponseRedirect('/bookmarks/')

    #     return render(request, 'login.html', {'form': form}) 


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
