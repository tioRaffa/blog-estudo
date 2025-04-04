from django.urls import path
from core.views import *


app_name = 'places'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('pages/', PagesView.as_view(), name='pages'),
    path('contato/', ContactPage.as_view(), name='contact'),
    path('detalhes/<int:pk>', DetailPage.as_view(), name='detail'),
    path('categoria/<int:id>', CategoryPage.as_view(), name='category'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]

