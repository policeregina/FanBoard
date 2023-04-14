from django import forms
from .models import Post, Comments


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_name', 'post_text', 'post_cat']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['com_text']
