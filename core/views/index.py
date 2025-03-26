from core.models.post import PostModel, CategoryModel
from django.views.generic import ListView
from django.shortcuts import render
from .cbv_base import BaseView
# Example view function

class IndexView(BaseView, ListView):
    model = PostModel
    context_object_name = 'posts'
    template_name = 'pages/index.html'
    
    
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True).order_by('?')
        return queryset