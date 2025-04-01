from django.shortcuts import render, redirect
from django.views.generic import View
from core.forms import LoginUserForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class LoginUserView(View):
    def render_page(self, request, form):
        
        context = {
            'form': form
        }
        return render(request, 'partials/content/modal/login.html', context=context)
    
    def get(self, request):
        form = LoginUserForm()
        
        return self.render_page(request, form)
    
    def post(self, request):
        form = LoginUserForm(request.POST)
        
        if form.is_valid():
            username_data = form.cleaned_data.get('username')
            password_data = form.cleaned_data.get('password')
            
            is_auth = authenticate(
                username=username_data,
                password=password_data
            )
            
            if is_auth is not None:
                login(request, is_auth)
                return redirect('places:index')
            
            else:
                return redirect('places:index')
        
        
        return render(request, 'pages/index.html')
    
    
@login_required(login_url='authors:login', redirect_field_name='next')
def logout_user(request):
    logout(request)
    return redirect('places:index')