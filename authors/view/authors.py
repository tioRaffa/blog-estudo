from django.shortcuts import render


def teste(request):
    return render(request, 'pages/profile_settings.html')