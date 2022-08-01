from sources.management.commands.baseanalysis import AnalysisCommand
from bs4 import BeautifulSoup
import requests
from sources.models import Source
from sources.models import Analysis
import datetime

class Command(AnalysisCommand):
    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
        parser.add_argument('url', type=str)
        parser.add_argument('finder', type=str)

    def handle(self, *args, **options):
        name = options["name"]
        url = options["url"]
        finder = options["finder"]

        print("Analyzing source: " + url)

        r = requests.get(url)
        html = r.text

        soup = BeautifulSoup(html, 'html.parser')
        article_titles = [x.text.strip() for x in soup.select(finder)]
        
        results = self.get_results(article_titles, name, 'fr')
        
        self.stdout.write(self.style.SUCCESS('Successfully ran analysis'))
        return