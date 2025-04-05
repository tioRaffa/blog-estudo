from django.urls import reverse_lazy
from core.models import PostModel, CategoryModel
from authors.forms import CreatePostForm
from django.views.generic import FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



@method_decorator(
    login_required(
        login_url='places:index',
        redirect_field_name='next',
    ), name='dispatch'
)
class CreatePostView(FormView):
    form_class = CreatePostForm
    template_name = 'pages/create_publication.html'
    success_url = reverse_lazy('authors:publications_crud')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'form': self.get_form(),
            'categories': CategoryModel.objects.all()
        })
        return context
    
    def form_valid(self, form):
        print(form.cleaned_data)
        post: PostModel = form.save(commit=False)
        post.is_published = False
        post.author = self.request.user
        
        category = self.request.POST.get('category')
        post.category = CategoryModel.objects.get(id=category)
        
        post.save()
        
        
        return super().form_valid(form)
    