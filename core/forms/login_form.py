from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class LoginUserForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'name':"username",
            'placeholder':"Nome de Usuario"
        }), required=True
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'name': "password",
            'placeholder': "Senha"
        }), required=True
    )
    
    def clean_username(self):
        username_data = self.cleaned_data.get('username')
        
        if not User.objects.filter(username=username_data).exists():
            raise forms.ValidationError(
                'Usuario nao encontrado!'
            )
        return username_data
    
    
         