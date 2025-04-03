from django.shortcuts import render, redirect 
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

def teste(request):
    return render(request, 'pages/create_publication.html')