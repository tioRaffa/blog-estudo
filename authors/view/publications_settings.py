from django.shortcuts import render

def teste(request):
    return render(request, 'pages/publications.html')