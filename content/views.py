from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'content/home.html', context)

def about(request):
    context = {}
    return render(request, 'content/about.html', context)
