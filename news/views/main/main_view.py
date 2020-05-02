from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from news.views.base_view import BaseView
from news.lib.constants import login_url


class MainView(LoginRequiredMixin, BaseView):
    login_url = login_url
    template_name = 'main.html'

    def get(self, request):
        return render(request, self.template_name)
