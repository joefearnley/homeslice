from django.views.generic import TemplateView


class SignupView(TemplateView):
    template_name = 'registration/registration_form.html'
