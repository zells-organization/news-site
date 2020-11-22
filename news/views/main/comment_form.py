from django.forms import ModelForm

from news.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ('author',)

    def save(self, commit=True):
        author = self.initial.get('author')
        to_post = self.cleaned_data.get('to_post')
        text = self.cleaned_data.get('text')
        comment = Comment(to_post=to_post, author=author, text=text)
        comment.save()
        return comment
