from django.urls import path
from authors.view import RegisterView, teste
app_name = 'authors'

urlpatterns = [
    path('profile/', teste, name='profile'),
    path('register/', RegisterView.as_view(), name='register_user'),
]
