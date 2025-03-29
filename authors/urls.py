from django.urls import path
from authors.view import teste, register

app_name = 'authors'

urlpatterns = [
    path('profile/', teste, name='profile'),
    path('register/', register, name='register_user'),
]
