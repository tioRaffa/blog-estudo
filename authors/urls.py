from django.urls import path
from authors.view import RegisterView, UpdateView, PublicationCrud
app_name = 'authors'

urlpatterns = [
    path('profile/', UpdateView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register_user'),
    path('publications/', PublicationCrud.as_view(), name='publications_crud'),
]
