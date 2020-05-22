from django.forms import ModelForm
from django import forms

from news.models import Post, User


class PostForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ('is_approved', 'author')

    def save(self, commit=True):
        author = User.objects.get(pk=self.request.user.id)
        self.author = author
        super(PostForm, self).save()
