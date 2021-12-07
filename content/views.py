from django.shortcuts import render
from content.models import Contact

def index(request):
    context = {}
    return render(request, 'content/home.html', context)

def about(request):
    context = {}
    return render(request, 'content/about.html', context)

def contact(request):
    context = {}
    return render(request, 'content/contact.html', context)

def error_404(request, exception):
    context = {}
    return render(request, 'content/404.html', context)

def error_500(request):
    context = {}
    return render(request, 'content/404.html', context)

def send_message(request):
    first_name = request.POST['first-name']
    last_name = request.POST['last-name']
    email = request.POST['email']
    message = request.POST['message']

    contact = Contact(first_name=first_name, last_name=last_name, email=email, message=message)
    contact.save()

    if(contact.id):
        notice = 'Message envoyé avec succès!'
    else:
        notice = 'Une erreur est survenue lors de l\'envoi du message!'

    context = {'notice': notice}
    return render(request, 'content/contact.html', context)