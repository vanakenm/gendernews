from sources.management.commands.baseanalysis import AnalysisCommand
from bs4 import BeautifulSoup
from sources.models import Analysis

class Command(AnalysisCommand):
    ## Need to work with BS4 for this to just do it on stuff inside <h3>
    def wrap(self, name, html):
        index = html.find(name)
        return html[:index] + "<mark>" + name + "</mark>" + html[index:]

    def handle(self, *args, **options):
        for analysis in Analysis.objects.all():
            html = analysis.html
            source = analysis.source
            name = source.name

            soup = BeautifulSoup(html, 'html.parser')
            article_titles = [x.text.strip() for x in soup.find_all(source.finder)]
            
            results = self.get_results(article_titles, name)

            analysis.results = results
            analysis.save()

        self.stdout.write(self.style.SUCCESS('Successfully ran analysis'))
        return