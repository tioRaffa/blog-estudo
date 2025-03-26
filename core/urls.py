from django.urls import path
from core.views import IndexView, contatc, PagesView, DetailPage


app_name = 'places'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contato/', contatc, name='contact'),
    path('detalhes/<int:pk>', DetailPage.as_view(), name='detail'),
    path('pages/', PagesView.as_view(), name='pages'),
]

