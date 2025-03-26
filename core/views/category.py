from django.views.generic import ListView
from core.models import PostModel, CategoryModel
from .cbv_base import BaseView

class CategoryPage(BaseView, ListView):
    model = PostModel
    template_name = 'pages/category.html'
    context_object_name = 'posts'
    
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
        
        context.update({
            'category_title': category_title
        })
        
        return context
    