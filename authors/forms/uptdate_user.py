from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from authors.models import Profile
from .validators import validation_username
import re

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        user_data = self.instance
        
        if User.objects.filter(username=username).exclude(pk=user_data.pk).exists():
            raise ValidationError(
                'Nome de usuario nao disponivel!'
            )
        
        if len(username) <3:
            raise ValidationError(
                'Nome de usuario deve conter pelo menos 3 caracteres'
            )
            
        if not re.match(r"^[a-zA-Z0-9_]+$", username):
            raise ValidationError(
                'O nome de usuario deve conter apenas letras, numeros e _'
            )
            
        if username.isdigit():
            raise ValidationError(
                'Nomde nao pode conter apenas numeros!'
            )
        return username
    
    def clean_email(self):
        email_data = self.cleaned_data.get('email')
        user_data = self.instance
        
        if User.objects.filter(email=email_data).exclude(pk=user_data.pk).exists():
            raise ValidationError(
                'Email ja Cadastrado, digite outro email!'
            )
        return email_data
    
    def clean_last_name(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        
        if first_name == last_name:
            raise ValidationError(
                'Ultimo nome nao pode ser igual ao Primeiro!'
            )
        return last_name
    

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'profile_pic',
            'bio'
        ]
        
    profile_pic = forms.FileInput()
    bio = forms.CharField(widget=forms.Textarea())