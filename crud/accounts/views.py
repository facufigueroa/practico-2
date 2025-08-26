from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')

class LogoutMessageView(TemplateView):
    template_name = 'accounts/logoutMessage.html'