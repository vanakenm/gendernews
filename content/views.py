from django.shortcuts import render
from content.models import Contact, ReleaseNote
from sources.models import ReportLine

def index(request):
    context = {}
    return render(request, 'content/home.html', context)

def about(request):
    context = {}
    return render(request, 'content/about.html', context)

def contact(request):
    context = {}
    return render(request, 'content/contact.html', context)

def notes(request):
    context = {
        'notes': ReleaseNote.objects.all().order_by('-created_at')
    }
    return render(request, 'content/notes.html', context)

def one_month(request):
    context = {
        'top5male': ReportLine.top5('male'),
        'top5female': ReportLine.top5('female')
    }

    return render(request, 'content/one-month.html', context)

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