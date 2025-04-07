from django.views.generic import ListView
from core.models import PostModel, CategoryModel, Comment
from .cbv_base import BaseView

class CategoryPage(BaseView, ListView):
    model = PostModel
    template_name = 'pages/category.html'
    context_object_name = 'posts'
    paginate_by = 6
    
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        
        category_id = self.kwargs.get('id')
        queryset = queryset.filter(
            category__id=category_id
        )
        
        return queryset
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        category_id = self.kwargs.get('id')
        category_title = CategoryModel.objects.get(id=category_id)
        
        post = context['posts']
        comments = Comment.objects.filter(post__in=post).order_by('created_at')
        
        context.update({
            'category_title': category_title,
            'comments': comments.count()
        })
        
        return context
    