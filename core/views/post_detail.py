from django.shortcuts import render

def post_detail(request):
    return render(request, 'pages/blog-details.html')