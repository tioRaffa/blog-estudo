from django import forms
from django.contrib.auth.models import User

from .validators import validation_password , validation_username

from django.contrib.auth.password_validation import CommonPasswordValidator
from django.core.exceptions import ValidationError
import re

class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput())
    last_name = forms.CharField(max_length=30, widget=forms.TextInput())
    username = forms.CharField(max_length=50, widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        
        
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
                'Email ja Cadastrado, digite outro email!',
                code='invalid'
            )
        return email_data
        
    
    def clean(self):
        cleaned_data = super().clean()
        
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        
        if password != password2:
            raise ValidationError(
                'Erro na confirmação de senha. Tente novamente!',
                code='invalid'
            )
        
        if first_name == last_name:
            raise ValidationError(
                'Primeiro nome e ultimo nao podem ser iguais! ',
                code='invalid'
            )