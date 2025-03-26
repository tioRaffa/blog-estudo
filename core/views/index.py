from core.models.post import PostModel
from django.views.generic import ListView
from django.shortcuts import render
from .cbv_base import BaseView
# Example view function

class IndexView(BaseView, ListView):
    model = PostModel
    context_object_name = 'posts'
    template_name = 'pages/index.html'
    
    
    