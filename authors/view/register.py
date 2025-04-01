from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse_lazy
from authors.forms import RegisterForm



class RegisterView(View):
    def render_page(self, request, form):
        context  = {
            'form': form,
        }
        return render(request, 'pages/register.html', context=context)
        
    def get(self, request):
        form = RegisterForm()
        
        return self.render_page(request, form)
    
    def post(self, request):
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/?login_modal=true')

        return self.render_page(request, form)