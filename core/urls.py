from django.urls import path
from .views import index, contatc
from django.conf.urls.static import static
from django.conf import settings

app_name = 'places'
urlpatterns = [
    path('', index, name='index'),
    path('contato', contatc, name='contact')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)