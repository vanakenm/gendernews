from sources.management.commands.baseanalysis import AnalysisCommand
import requests
from sources.models import Source, ReportLine
import datetime
import string
import csv

def simplify_gender(gender):
  if(gender == "male" or gender == "female" or gender == "andy"):
    return gender
  if(gender == "mostly_male"):
    return "male"
  if(gender == "mostly_female"):
    return "female"

class Command(AnalysisCommand):
    def handle(self, *args, **options):
        with open('report.csv', 'w') as csvfile:
          writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
          writer.writerow(["source","url", "date", "gender", "name"])
          for source in Source.objects.all():
              url = source.url
              source_name = source.name
              for analysis in source.analysis_set.all():
                  date = analysis.date
                  results = analysis.results
                  names = results["names"]
                  for name in names:
                    gender = name["gender"]
                    gender = simplify_gender(gender)
                    person_name = name["name"]
                    person_name = person_name.translate(str.maketrans('', '', string.punctuation))
                    person_name = person_name.strip()
                    writer.writerow([source_name, url, date, gender, person_name])
                    report_line = ReportLine.objects.create(source_name=source_name, gender=gender, name=person_name, date=date)
                    report_line.save()