from django.contrib.auth.mixins import PermissionRequiredMixin

from news.library import premoderate_codename
from news.models import Post
from news.views import BaseView
from django.shortcuts import render, redirect


class PremoderationView(PermissionRequiredMixin, BaseView):
    template_name = 'premoderation.html'
    permission_denied_message = "You don't have permission to access this page"
    permission_required = [premoderate_codename]

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
