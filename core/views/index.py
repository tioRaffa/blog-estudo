from core.models.post import PostModel, Comment
from django.views.generic import ListView
from django.shortcuts import render
from .cbv_base import BaseView
# Example view function

class IndexView(BaseView, ListView):
    model = PostModel
    context_object_name = 'posts'
    template_name = 'pages/index.html'
    paginate_by = 4
    
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        post = context['posts']
        comments = Comment.objects.filter(post__in=post).order_by('created_at')
        context.update({
            'comments': comments.count()
        })
        
        return context