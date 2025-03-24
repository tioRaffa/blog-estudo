from django.shortcuts import render

def contatc(request):
    return render(request, 'pages/contact.html')