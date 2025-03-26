from core.models.post import PostModel, CategoryModel
from django.views.generic import DetailView
from .cbv_base import BaseView


class DetailPage(BaseView, DetailView):
    model = PostModel
    context_object_name = 'post'
    template_name = 'pages/blog-details.html'
    
    
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(id=self.kwargs.get('pk'))
        
        return queryset
    