from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from news.views.registration.registration_form import RegistrationForm


class RegistrationView(View):
    template_name = 'registration.html'
    registration_form = RegistrationForm

    def get(self, request):
        form = self.registration_form()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.registration_form(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=email, password=raw_password)
            login(request, user)
            return redirect('main')
        return render(request, self.template_name, {'form': form})
