from django.views.generic import ListView
from django.shortcuts import render
from core.models.post import PostModel, CategoryModel
# Example view function

class IndexView(ListView):
    model = PostModel
    template_name = 'pages/index.html'
    context_object_name = 'posts'
    
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True).order_by('?')
        return queryset
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        category = CategoryModel.objects.all()
        context.update({
            'categories': category,
        })
        return context
    