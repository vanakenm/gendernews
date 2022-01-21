from sources.management.commands.baseanalysis import AnalysisCommand
from bs4 import BeautifulSoup
from sources.models import Source

class Command(AnalysisCommand):
    def add_arguments(self, parser):
        parser.add_argument('source_name', type=str)

    def handle(self, *args, **options):
        source_name = options["source_name"]
        print("Refreshing source: " + source_name)

        source = Source.objects.get(name=source_name)

        for analysis in source.analysis_set.all():
            print("Refreshing analysis: " + analysis.date.strftime("%Y-%m-%d"))
            html = analysis.html
            source = analysis.source
            name = source.name

            soup = BeautifulSoup(html, 'html.parser')
            article_titles = [x.text.strip() for x in soup.find_all(source.finder)]
            
            results = self.get_results(article_titles, name, source.language())

            analysis.results = results
            analysis.save()

        self.stdout.write(self.style.SUCCESS('Successfully ran analysis'))
        return