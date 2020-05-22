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
        author = self.initial.get('author')
        is_approved = False

        if author.has_perm('news.post_no_premoderation'):
            is_approved = True

        post = Post(
            author=author,
            title=self.cleaned_data.get('title'),
            text=self.cleaned_data.get('text'),
            is_approved=is_approved
        )

        post.save()
        return post
