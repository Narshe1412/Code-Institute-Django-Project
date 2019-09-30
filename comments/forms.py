from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """ Creates a form the user can use to publish comments """
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
          'content': forms.Textarea(attrs={'rows':3}),
        }