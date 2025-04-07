from core.models.post import PostModel, CategoryModel, Comment
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
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        post = self.object
        comments = Comment.objects.filter(post=post).order_by('created_at')
        context.update({
            'comments': comments
        })
        
        return context
    
    