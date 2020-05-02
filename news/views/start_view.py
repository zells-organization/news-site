from django.http import HttpResponse
from django.views import View
from django.shortcuts import render


class StartView(View):
    template_name = 'hello.html'

    def get(self, request):
        return render(request, self.template_name)
