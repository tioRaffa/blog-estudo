from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from authors.forms import RegisterForm



class RegisterView(FormView):
    template_name = 'pages/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy("authors:register_user")
    
    def form_valid(self, form, *args, **kwargs):
        user = form.save()
        
        return super().form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form):
        
        if 'username' in form.errors:
            form.cleaned_data['username'] = ''
        
        if 'email' in form.errors:
            form.cleaned_data['email'] = ''
        
        if 'first_name' in form.errors:
            form.cleaned_data['last_name'] = ''
        
        if 'password' in form.errors:
            form.cleaned_data['password2'] = ''
        
        return self.render_to_response({'form': form})
    