from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponseRedirect


class UserLoginView(TemplateView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "You are now logged-In, welcome")
            return HttpResponseRedirect('/bookmarks/')

        return render(request, 'login.html', {'form': form}) 


class UserRegisterView(TemplateView):
    template_name = 'register.html'
