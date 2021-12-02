from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'content/home.html', context)

def about(request):
    context = {}
    return render(request, 'content/about.html', context)

def contact(request):
    context = {}
    return render(request, 'content/contact.html', context)

def send_message(request):
    context = {
        "notice": 'Message sent successfully!'
    }
    return render(request, 'content/contact.html', context)