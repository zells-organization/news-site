from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from ..base_view import BaseView
from .login_form import LoginForm


class LoginView(BaseView):
    template_name = 'login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        return HttpResponse("Response")
