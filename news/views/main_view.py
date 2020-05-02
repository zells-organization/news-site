from django.http import HttpResponse
from django.views import View
from django.shortcuts import render


class MainView(View):
    template_name = 'main.html'

    def get(self, request):
        return render(request, self.template_name)
