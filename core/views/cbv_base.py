from core.models import PostModel, CategoryModel

class BaseView:
    
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True).order_by('?')
        
        return queryset
    
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        category = CategoryModel.objects.all()
        recent = PostModel.objects.filter(is_published=True).order_by('-id')[:3]
        
        context.update({
            'categories': category,
            'recents': recent
        })
        
        return context