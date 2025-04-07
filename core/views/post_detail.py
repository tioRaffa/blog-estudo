from core.models.post import PostModel, CategoryModel, Comment
from core.forms import CommentsForm
from django.views.generic import DetailView
from .cbv_base import BaseView
from django.shortcuts import redirect


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
            'comments': comments,
            'form': CommentsForm
        })
        
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentsForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = self.request.user
        
            comment.save()
            return redirect('places:detail', pk=self.object.pk)
        
        context = self.get_context_data()
        context['form'] = form
        
        return self.render_to_response(context)
    
    