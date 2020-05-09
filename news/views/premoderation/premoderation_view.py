from news.models import Post
from news.views import BaseView
from django.shortcuts import render


class PremoderationView(BaseView):
    template_name = 'premoderation.html'

    def get(self, request):
        posts = Post.objects.all()
        return render(request, self.template_name, {'posts': posts})
