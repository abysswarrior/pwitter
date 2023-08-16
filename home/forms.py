from django import forms
from .models import Post, Comment


class PostCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body', 'title')


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }


class CommentReplyForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'col-md-5', 'rows': "2"}), label='')

    class Meta:
        model = Comment
        fields = ('body',)


class PostSearchForm(forms.Form):
    search = forms.CharField()