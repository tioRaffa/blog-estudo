from django.shortcuts import render, redirect
from django.views.generic import View
from core.models import PostModel, CategoryModel
from authors.forms import UpdatePostForm
from django.contrib import messages
from django.shortcuts import get_object_or_404

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required




@method_decorator(
    login_required(
        login_url='places:index',
        redirect_field_name='next'
    ), name='dispatch'
)
class UpdatePostModel(View):
    
    def render_page(self, request, form, categories, post):
        context = {
            'form': form,
            'categories': categories,
            'post': post
        }
        return render(request, "pages/update_publication.html", context=context)
    
    
    def get(self, request, id):
        post = get_object_or_404(PostModel, id=self.kwargs['id'], author=self.request.user)
        categories = CategoryModel.objects.all()
        form = UpdatePostForm()
        
        return self.render_page(request, form=form, categories=categories, post=post)
    
    
    def post(self, request, id):
        post_instance = get_object_or_404(PostModel, id=id, author=request.user)
        form = UpdatePostForm(request.POST, request.FILES, instance=post_instance)

        if form.is_valid():
            post = form.save(commit=False)
            post.is_published = False
            post.author = request.user

            category_id = request.POST.get('category')
            post.category = get_object_or_404(CategoryModel, id=category_id)

            post.save()
            messages.success(request, 'Publicação alterada com sucesso! Após a verificação da administração, será liberada!')
            return redirect('authors:publications_crud')
        else:
            categories = CategoryModel.objects.all()
            return self.render_page(request, form=form, categories=categories, post=post_instance)
        
    
