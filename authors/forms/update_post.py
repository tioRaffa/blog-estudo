from django import forms
from core.models import PostModel

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'image', 'description', 'recomendations', 'category', 'cost']