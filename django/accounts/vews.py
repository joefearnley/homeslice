from django.views.generic import TemplateView


class SignupView(TemplateView):
    template_name = 'home.html'
