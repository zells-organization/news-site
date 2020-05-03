from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from .login_form import LoginForm


class LoginView(View):
    template_name = 'login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return self.__login_user(request, form)

        return HttpResponse("Response")

    def __login_user(self, request, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        try:
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                return redirect('main')
        except ValidationError as e:
            for field, error in e.args[0].items():
                form.errors[field] = error
            return render(request, self.template_name, {'form': form})
