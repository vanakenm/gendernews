from spacy.lang.fr.stop_words import STOP_WORDS
from django.core.management.base import BaseCommand

from sources.models import Analysis

class Command(BaseCommand):
  def handle(self, *args, **options):
    all = Analysis.objects.all()

    all_words = []
    for analysis in all:
      titles = analysis.results["titles"]
      for title in titles:
        words = title.split(" ")
        all_words += words
    print(STOP_WORDS)
    print(all_words)