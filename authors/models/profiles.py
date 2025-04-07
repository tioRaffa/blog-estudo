from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    author = models.OneToOneField(User, verbose_name=("Usuario"), on_delete=models.CASCADE)
    profile_pic = models.ImageField(("Foto de Perfil"), default='profile_image/image/profile.png', upload_to='profile_image/image/%y/%m/%d')
    

    def __str__(self):
        return self.author.username

    