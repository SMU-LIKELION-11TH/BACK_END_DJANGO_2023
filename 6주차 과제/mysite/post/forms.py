from django import forms

class PostForm(forms.Form):
    title = forms.CharField(label='Title')
    content = forms.CharField(label='Content', widget=forms.Textarea)
