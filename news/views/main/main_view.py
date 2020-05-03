from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from news.views.base_view import BaseView


class MainView(BaseView):
    template_name = 'main.html'

    def get(self, request):
        return render(request, self.template_name)
