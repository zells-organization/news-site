from django.shortcuts import render, redirect

from news.models import User
from news.views import BaseView
from news.views.create_post.post_form import PostForm


class CreatePostView(BaseView):
    template_name = 'create_post.html'
    form_class = PostForm

    def get(self, request):
        author = User.objects.get(pk=request.user.id)
        form = self.form_class(initial={'author': author})
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        author = User.objects.get(pk=request.user.id)
        form = self.form_class(request.POST, initial={'author': author})
        if form.is_valid():
            form.save()
            return redirect('main')
        return render(request, self.template_name, {'form': form})
