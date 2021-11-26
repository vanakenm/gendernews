from django.http.response import HttpResponse
from django.shortcuts import render
from sources.models import Analysis, Source
from django.template import loader


def index(request):
    sources = Source.objects.all()
    template = loader.get_template('sources/index.html')
    context = {
        'sources': sources,
    }
    return render(request, 'sources/index.html', context)

def detail(request, source_id):
    source = Source.objects.get(pk=source_id)
    analyses = source.analysis_set.all()
    context = {
        'source': source,
        'analyses': analyses,
    }
    return render(request, 'sources/detail.html', context)

def screenshot(request, source_id, analysis_id):
    analysis = Analysis.objects.get(pk=analysis_id)
    html = analysis.html
    response =  HttpResponse(html)
    response.headers["X-Frame-Options"] = "ALLOWALL"

    return response
