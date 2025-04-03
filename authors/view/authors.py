from django.shortcuts import render, redirect
from django.views.generic import View
from authors.forms import UpdateUserForm, UpdateProfileForm

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(
    login_required(
        login_url='places:index',
        redirect_field_name='next'
    ), name='dispatch'
)
class UpdateView(View):
    def render_page(self, request, form_user, form_profile):
        context = {
            'form_user': form_user,
            'form_profile': form_profile
        }
        
        return render(request, 'pages/profile_settings.html', context=context)
    
    def get(self, request):
        form_user = UpdateUserForm(instance=request.user)
        form_profile = UpdateProfileForm(instance=request.user.profile)
        
        return self.render_page(request, form_profile=form_profile, form_user=form_user)
    
    def post(self, request):
        form_user = UpdateUserForm(request.POST, instance=request.user)
        form_profile = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        
        if form_profile.is_valid() and form_user.is_valid():
            form_user.save()
            form_profile.save()
            print(form_user.errors)
            print(form_profile.errors)
            
            return redirect('places:index')
        print(form_user.errors)
        print(form_profile.errors)
        return self.render_page(request, form_profile=form_profile, form_user=form_user)