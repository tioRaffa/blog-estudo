from django import forms
from django.contrib.auth.models import User

from .validators import validation_password , validation_username

from django.contrib.auth.password_validation import CommonPasswordValidator
from django.core.exceptions import ValidationError
import re


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': 'ex: Ab12345678!'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': 'Confirme sua Senha'}),
    )
    username = forms.CharField(
        max_length=50,
        min_length=2,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'input-box',
            'placeholder': 'Digite seu Nome de Usuário',
        })
    )
    
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Digite seu Nome', }),
            'last_name': forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Digite seu Último Nome',}),
            'email': forms.EmailInput(attrs={'class': 'input-box', 'placeholder': 'ex: exemploemail@gmail.com',}),
        }
        
        
    def clean_password(self):
        password_data = self.cleaned_data.get('password')
        return validation_password(password_data)
    
    def clean_username(self):
        username = self.cleaned_data.get('username', '').strip().lower()
        return validation_username(username)
    
    def clean_email(self):
        email_data = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email_data).exists():
            raise ValidationError(
                'Email ja Cadastrado, digite outro email!'
            )
        return email_data
        
    
    def clean_password2(self):
        password_data = self.cleaned_data.get('password')
        password2_data = self.cleaned_data.get('password2')
        
        if password_data != password2_data:
            raise ValidationError(
                'Confirme sua senha Corretamente!'
            )
        return password2_data
            
    def clean_last_name(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        
        if first_name == last_name:
            raise ValidationError(
                'Ultimo nome nao pode ser igual ao Primeiro!'
            )
        return last_name