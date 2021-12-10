from django.core.management.base import BaseCommand
from sources.models import Source
from sources.models import Analysis
import datetime

class Command(BaseCommand):
    def handle(self, *args, **options):
      print("Cleaning up old empty results")
      empty_analysis = Analysis.objects.filter(results__names=[])
      for analysis in empty_analysis:
          print(analysis.source.name + " - " + analysis.date.strftime("%Y-%m-%d"))
          analysis.delete()
      return