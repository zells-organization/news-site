from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from news.lib.constants import login_url


class BaseView(LoginRequiredMixin, View):
    login_url = login_url

