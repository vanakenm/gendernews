from sources.management.commands.baseanalysis import AnalysisCommand
from bs4 import BeautifulSoup
import requests
from sources.models import Source
from sources.models import Analysis
import datetime

class Command(AnalysisCommand):
    def handle(self, *args, **options):
        for source in Source.objects.all():
            url = source.url
            name = source.name

            r = requests.get(url)
            html = r.text

            soup = BeautifulSoup(html, 'html.parser')
            article_titles = [x.text.strip() for x in soup.find_all(source.finder)]
            
            results = self.get_results(article_titles, name)
            
            analysis = Analysis.objects.create(source=source, html=html, date=datetime.datetime.now(), results=results)
            analysis.save()

        self.stdout.write(self.style.SUCCESS('Successfully ran analysis'))
        return