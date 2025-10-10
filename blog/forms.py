from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):

    def Meta():
        model = Post
        fields = ('author', 'title', 'text')

        # Widget custom editing and styling
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})

        }


class CommentForm(forms.ModelForm):

    def Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }