from django.core.management.base import BaseCommand
from twitter import *
import datetime
from dotenv import load_dotenv
from sources.models import Source, Analysis
import os

load_dotenv()  # take environment variables from .env.

class Command(BaseCommand):
    def handle(self, *args, **options):
        t = Twitter(
            auth=OAuth(os.environ["NC_TOKEN"] ,os.environ["NC_TOKEN_SECRET"], os.environ["NC_CONSUMER_KEY"], os.environ["NC_CONSUMER_SECRET"]))

        sources = Source.objects.filter(twitter_handle__isnull=False).all()

        for source in sources:
            analysis = source.last_analysis()
            stats = analysis.stats()
            print(source.twitter_handle)
            print(stats)

            url = "https://www.newscheck.info/sources/{}/analysis/{}".format(source.id, analysis.id)

            status = "📊 Aujourd'hui {} a publié {} articles avec un nom identifiable - dont {} de femmes ({}%) et {} d'hommes ({}%). Details: {}. Source: {}".format(
                source.twitter_handle, stats["total"], stats["female"], stats["femalepc"], stats["male"], stats["malepc"], url, source.url
            )

            print(status)

            t.statuses.update(
                status=status)
