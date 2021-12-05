import datetime
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

def detail(request, source_id, analysis_id):
    source = Source.objects.get(pk=source_id)
    analysis = Analysis.objects.get(pk=analysis_id)
    context = {
        'source': source,
        'analysis': analysis,
    }
    return render(request, 'sources/detail.html', context)

def screenshot(request, source_id, analysis_id):
    analysis = Analysis.objects.get(pk=analysis_id)
    html = analysis.html
    response =  HttpResponse(html)
    response.headers["X-Frame-Options"] = "ALLOWALL"

    return response

def dashboard(request):
    sources = Source.objects.all()
    today = datetime.datetime.today()
    date_req = request.GET.get("date", None)
    if(date_req):
      date = datetime.datetime.strptime(date_req, "%Y-%m-%d")
      analyses = [(source, source.last_analysis(date)) for source in sources]
    else:
      date = today
      analyses = [(source, source.last_analysis()) for source in sources]
      
    
    context = {
        'analyses': analyses,
        'day': date,
        'next_day': date + datetime.timedelta(days=1) if today > date + datetime.timedelta(days=1) else None,
        'previous_day': date - datetime.timedelta(days=1),
    }
    return render(request, 'sources/dashboard.html', context)