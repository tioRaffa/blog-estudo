from django.shortcuts import render
from core.models import PostModel
from django.views.generic import ListView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required




@method_decorator(
    login_required(
        login_url='places:index',
        redirect_field_name='next'
    ), name='dispatch'
)
class PublicationCrud(ListView):
    model = PostModel
    template_name = 'pages/publications.html'
    context_object_name = 'post_published'
    paginate_by = 4
    ordering = '-id'
    
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(author=self.request.user, is_published=True)
        
        return queryset

    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        not_published = PostModel.objects.filter(author=self.request.user, is_published=False)
        context.update({
            'post_not_published': not_published
        })
        
        return context
    
    
    
    