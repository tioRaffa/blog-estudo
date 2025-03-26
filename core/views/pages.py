from django.views.generic import ListView
from core.models import PostModel
from .cbv_base import BaseView

class PagesView(BaseView, ListView):
    model = PostModel
    context_object_name = 'posts'
    template_name = 'pages/page_publication.html'
    
    