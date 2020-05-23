from news.models import Post
from news.views import BaseView
from django.shortcuts import render, redirect


class PremoderationView(BaseView):
    template_name = 'premoderation.html'

    def get(self, request):
        posts = Post.objects.all()
        return render(request, self.template_name, {'posts': posts})

    def post(self, request):
        data = request.POST
        post = Post.objects.get(pk=data.get('post_id'))

        if 'approve' in data:
            post.is_approved = True
        if 'decline' in data:
            post.is_approved = False
        post.save()
        return redirect('premoderation')
