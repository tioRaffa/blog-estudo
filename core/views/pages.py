from django.shortcuts import render

def pages(request):
    return render(request, 'pages/pages.html')