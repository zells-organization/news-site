from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from news.models import Post, User
from news.views.base_view import BaseView
from news.views.main.comment_form import CommentForm


class MainView(BaseView):
    template_name = 'main.html'
    form_class = CommentForm

    def get(self, request):
        posts = Post.objects.filter(is_approved=True)
        return render(request, self.template_name, {'posts': posts})

    def post(self, request):
        author = User.objects.get(pk=request.user.id)
        form = self.form_class(request.POST, initial={'author': author})
        if form.is_valid():
            form.save()
            return redirect('main')
        posts = Post.objects.filter(is_approved=True)

        return render(request, self.template_name, {'posts': posts})
