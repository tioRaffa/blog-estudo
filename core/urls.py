from django.urls import path
from .views import IndexView, contatc, pages, DetailPage


app_name = 'places'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contato/', contatc, name='contact'),
    path('detalhes/<int:pk>', DetailPage.as_view(), name='detail'),
    path('pages/', pages, name='pages'),
]

