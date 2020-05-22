from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from news.models import Post
from news.views.base_view import BaseView


class MainView(BaseView):
    template_name = 'main.html'

    def get(self, request):
        posts = Post.objects.filter(is_approved=True)
        return render(request, self.template_name, {'posts': posts})
