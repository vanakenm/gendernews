from django.core.management.base import BaseCommand, CommandError
import spacy
from bs4 import BeautifulSoup
import requests
from sources.models import Source
from sources.models import Analysis
import gender_guesser.detector as gender
import datetime

class Command(BaseCommand):
    help = 'Run analysis for all sources'
    nlp = spacy.load("fr_core_news_sm")
    d = gender.Detector()

    ## Need to work with BS4 for this to just do it on stuff inside <h3>
    def wrap(self, name, html):
        index = html.find(name)
        return html[:index] + "<mark>" + name + "</mark>" + html[index:]

    def handle(self, *args, **options):
        for source in Source.objects.all():
            results = []
            url = source.url
            name = source.name

            r = requests.get(url)
            html = r.text

            soup = BeautifulSoup(html, 'html.parser')
            article_titles = [x.text.strip() for x in soup.find_all(source.finder)]
            
            for(title) in article_titles:
                doc = self.nlp(title)
                for word in doc.ents:
                    if(word.label_ == "PER"):
                        gender = self.d.get_gender(word.text.split(" ")[0])
                        if(gender != "unknown"):
                            print(name + ":" + word.text + " - " + gender)
                            results.append({"name": word.text, "gender": gender, "source": name})
                            # html = self.wrap(word.text, html)
            
            analysis = Analysis.objects.create(source=source, html=html, date=datetime.datetime.now(), results=results)
            analysis.save()

        self.stdout.write(self.style.SUCCESS('Successfully ran analysis'))