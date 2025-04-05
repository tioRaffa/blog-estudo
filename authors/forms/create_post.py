from django import forms
from core.models import PostModel

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = [
            'title', 'image', 'description', 'recommendations', 'category'
        ]