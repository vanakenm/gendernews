from sources.management.commands.baseanalysis import AnalysisCommand
from bs4 import BeautifulSoup
from sources.models import Analysis

class Command(AnalysisCommand):
    def handle(self, *args, **options):
        for analysis in Analysis.objects.all():
            html = analysis.html
            source = analysis.source
            name = source.name

            soup = BeautifulSoup(html, 'html.parser')
            article_titles = [x.text.strip() for x in soup.select(source.finder)]
            
            results = self.get_results(article_titles, name, source.language())

            analysis.results = results
            analysis.save()

        self.stdout.write(self.style.SUCCESS('Successfully ran analysis'))
        return