from django.http import HttpResponse
from django.views import View
from django.shortcuts import render


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)
