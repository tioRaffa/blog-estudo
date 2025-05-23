from django.urls import path
from authors.view import *
app_name = 'authors'

urlpatterns = [
    path('profile/', UpdateView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register_user'),
    path('publications/', PublicationCrud.as_view(), name='publications_crud'),
    path('create/', CreatePostView.as_view(), name='create'),
    path('publicação/configuração/<int:id>', UpdatePostModel.as_view(), name='update'),
    path('delete/<int:id>', DeletePost.as_view(), name='delete'),
]
