from sources.management.commands.baseanalysis import AnalysisCommand
from bs4 import BeautifulSoup
import requests
from sources.models import Source
from sources.models import Analysis
import datetime

class Command(AnalysisCommand):
    def add_arguments(self, parser):
        parser.add_argument('source_name', type=str)

    def handle(self, *args, **options):
        source_name = options["source_name"]

        print("Analyzing source: " + source_name)

        source = Source.objects.get(name=source_name)
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