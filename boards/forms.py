from django import forms
from .models import Topic, Post

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs = {'rows':5, 'placeholder': 'What\'s in your mind?'}
        ),
        max_length=4000,
        help_text = 'This must be at most 4000 in length.'
        )

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]