from django import forms
from core.models import Comment

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'message'
        ]
        
    message = forms.CharField(widget=forms.Textarea())
    