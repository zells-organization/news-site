from django.shortcuts import render

from news.views import BaseView


class ProfileView(BaseView):
    template_name = "profile.html"

    def get(self, request):
        return render(request, self.template_name)
