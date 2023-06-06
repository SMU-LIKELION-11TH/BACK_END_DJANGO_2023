from django import forms

from posts.models import Post
from comments.models import Comment
from recomments.models import Recomment

class PostCreateForm(forms.ModelForm):
    category = forms.TypedChoiceField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], coerce=int)

    class Meta:
        model = Post
        fields = ['category', 'title', 'content']

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
