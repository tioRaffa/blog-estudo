from django.views.generic import ListView
from core.models import PostModel, Comment
from .cbv_base import BaseView

class PagesView(BaseView, ListView):
    model = PostModel
    context_object_name = 'posts'
    template_name = 'pages/page_publication.html'
    paginate_by = 8
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        post = context['posts']
        comments = Comment.objects.filter(post__in=post).order_by('created_at')
        context.update({
            'comments': comments.count()
        })
        
        return context