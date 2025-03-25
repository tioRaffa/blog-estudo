from django.urls import path
from .views import IndexView, contatc, post_detail, pages
from django.conf.urls.static import static
from django.conf import settings

app_name = 'places'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contato/', contatc, name='contact'),
    path('detalhes/', post_detail, name='detail'),
    path('pages/', pages, name='pages'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)