from django.shortcuts import render
from sources.models import Source
from django.template import loader


def index(request):
    sources = Source.objects.all()
    template = loader.get_template('sources/index.html')
    context = {
        'sources': sources,
    }
    return render(request, 'sources/index.html', context)

