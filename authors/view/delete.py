from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from core.models import PostModel
from django.contrib import messages

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(
    login_required(
        login_url='places:index',
        redirect_field_name='next'
    ), name='dispatch'
)
class DeletePost(View):
    def get_post(self, id):
        return get_object_or_404(PostModel, id=id)
    
    def get(self, request, id):
        post_data = self.get_post(id=id)
        
        context = {
            'post': post_data
        }
        
        return render(request, 'partials/content/modal/delete_form.html', context=context)
    
    def post(self, request, id):
        post_data = self.get_post(id=id)
        post_data.delete()
        
        messages.success(request, 'Publicação apagada com sucesso!')
        
        return redirect('authors:publications_crud')