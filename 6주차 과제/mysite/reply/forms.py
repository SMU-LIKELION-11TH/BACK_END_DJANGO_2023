from django import forms

class ReplyForm(forms.Form):
    content = forms.CharField(label='Content', widget=forms.Textarea)
